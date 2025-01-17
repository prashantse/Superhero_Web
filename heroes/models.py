from django.db import models
from django.conf import settings

class Superhero(models.Model):
    name = models.CharField(max_length=255)
    universe = models.CharField(max_length=255)
    powers = models.TextField() # will be a simple text field
    first_power = models.CharField(max_length=255, blank=True,null=True)
    story = models.TextField(blank = True, null=True)
    real_creator = models.CharField(max_length = 255, blank=True,null=True)
    listed_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null = True,blank=True, related_name='listed_superheroes')
    movies = models.TextField(blank = True, null = True)
    shows = models.TextField(blank = True, null=True)
    main_image = models.ImageField(upload_to='superhero_main_images/')
    images = models.ManyToManyField('SuperheroImage', blank=True)
    wisdom = models.IntegerField(default=50)
    raw_power = models.IntegerField(default=50)
    combat_skills = models.IntegerField(default=50)
    durability = models.IntegerField(default=50)
    intelligence = models.IntegerField(default=50)
    agility = models.IntegerField(default = 50)

    allies = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='is_ally_of')
    enemies = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='is_enemy_of')
    alter_ego = models.CharField(max_length=255, blank=True, null=True)
    base = models.CharField(max_length=255, blank=True, null=True)
    comic_series = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
      return self.name
      
class SuperheroImage(models.Model):
  image = models.ImageField(upload_to='superhero_images/')

  def __str__(self):
    return f"Image for {self.image.url}"

class Comment(models.Model):
    superhero = models.ForeignKey(Superhero, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.superhero.name}"
class Like(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  superhero = models.ForeignKey(Superhero, on_delete=models.CASCADE,related_name='likes')

  def __str__(self):
    return f"like by {self.user.username} on {self.superhero.name}"