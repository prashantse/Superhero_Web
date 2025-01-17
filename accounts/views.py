from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm,LoginForm
from .models import CustomUser
from heroes.models import Superhero

def register_user(request):
  if request.method == 'POST':
    form = RegisterUserForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('hero-list')
  else:
    form = RegisterUserForm()

  return render(request, 'accounts/register.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hero-list')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('hero-list')

@login_required
def profile_view(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)
    superheroes = Superhero.objects.all()

    if request.method == "POST":
      superfan_id = request.POST.get("superfan")
      fan_ids = request.POST.getlist("fan")
      user.superfan_of = Superhero.objects.get(pk = superfan_id) if superfan_id else None
      user.fan_of.set(Superhero.objects.filter(pk__in=fan_ids))
      user.save()
      return redirect('profile', pk = user.pk)

    context = {'user': user,'superheroes':superheroes}
    return render(request, 'accounts/profile.html', context)