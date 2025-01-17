from django.shortcuts import render,redirect,get_object_or_404
from .models import Superhero,SuperheroImage,Comment,Like
from .forms import SuperheroForm,ImageForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Q

def superhero_list(request):
    search_query = request.GET.get('search')
    if search_query:
        superheroes = Superhero.objects.filter(
            Q(name__icontains=search_query) |
            Q(universe__icontains=search_query) |
            Q(powers__icontains=search_query)
        )
    else:
        superheroes = Superhero.objects.all()

    universes = Superhero.objects.values_list('universe', flat=True).distinct()

    context = {'superheroes': superheroes, 'universes': universes}
    return render(request, 'heroes/superhero_list.html', context)

@login_required
def add_superhero(request):
  if request.method == "POST":
    form = SuperheroForm(request.POST,request.FILES)
    if form.is_valid():
      new_superhero = form.save(commit=False)
      new_superhero.created_by = request.user
      new_superhero.save()
      return redirect('hero-detail', pk = new_superhero.pk)
  else:
    form = SuperheroForm()

  context = {'form':form}
  return render(request,'heroes/superhero_form.html',context)

def superhero_detail(request,pk):
  superhero = get_object_or_404(Superhero,pk=pk)
  images = superhero.images.all()
  comments = superhero.comments.all()
  user_liked = False
  if request.user.is_authenticated:
      user_liked = Like.objects.filter(superhero=superhero, user=request.user).exists()

  context = {'superhero': superhero,
               'images':images,
               'user_liked': user_liked,
               'comments':comments
               }
  return render(request,'heroes/superhero_detail.html', context)

@login_required
def add_image(request,pk):
  superhero = get_object_or_404(Superhero, pk = pk)
  if request.method == "POST":
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      image = form.save()
      superhero.images.add(image)
      return redirect('hero-detail',pk=pk)
  else:
      form = ImageForm()

  context = {'form':form,'superhero':superhero}
  return render(request,'heroes/superhero_form.html', context)

@login_required
def add_comment(request,pk):
  superhero = get_object_or_404(Superhero, pk = pk)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.superhero = superhero
        comment.user = request.user
        comment.save()
        return redirect('hero-detail', pk = pk)
  else:
        form = CommentForm()
  context = {'form':form,'superhero':superhero}
  return render(request,'heroes/comment_form.html',context)

@login_required
def like_superhero(request,pk):
  superhero = get_object_or_404(Superhero, pk=pk)
  if request.user.is_authenticated:
      liked = Like.objects.filter(user = request.user, superhero = superhero)
      if liked:
          liked.delete()
      else:
         Like.objects.create(user = request.user, superhero=superhero)
  return redirect('hero-detail',pk=pk)

def leaderboard_view(request):
  context = {'data': [
        {'name': 'Person 1', 'score': 100},
        {'name': 'Person 2', 'score': 90},
        {'name': 'Person 3', 'score': 80},
        {'name': 'Person 4', 'score': 70},
    ]}
  return render(request, 'heroes/leaderboard.html',context)

def superfan_view(request):
    superfan_data = (
        Superhero.objects.annotate(fan_count=Count("superfans"))
        .order_by("-fan_count")
        .values("name", "fan_count")
    )
    context = { 'superfans': superfan_data, }

    return render(request,'heroes/superfan.html',context)


def compare_superheroes(request):
    hero1_id = request.GET.get('hero1')
    hero2_id = request.GET.get('hero2')

    hero1 = get_object_or_404(Superhero, id=hero1_id) if hero1_id else None
    hero2 = get_object_or_404(Superhero, id=hero2_id) if hero2_id else None

    print(f"Hero 1: {hero1}")  # Debugging
    print(f"Hero 2: {hero2}")  # Debugging

    return render(request, 'heroes/compare_heroes.html', {
        'hero1': hero1,
        'hero2': hero2,
        'superheroes': Superhero.objects.all(),
    })