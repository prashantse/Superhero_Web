from django import forms
from .models import Superhero,SuperheroImage,Comment

class SuperheroForm(forms.ModelForm):
  class Meta:
    model = Superhero
    fields = ['name','universe','powers','first_power','story','real_creator','movies','shows','main_image', 'wisdom', 'raw_power', 'combat_skills', 'durability', 'intelligence','agility']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-input'}),
      'universe': forms.TextInput(attrs={'class': 'form-input'}),
      'powers': forms.Textarea(attrs={'class': 'form-textarea'}),
      'first_power': forms.TextInput(attrs={'class': 'form-input'}),
      'story': forms.Textarea(attrs={'class': 'form-textarea'}),
      'real_creator': forms.TextInput(attrs={'class': 'form-input'}),
      'movies': forms.Textarea(attrs={'class': 'form-textarea'}),
      'shows': forms.Textarea(attrs={'class': 'form-textarea'}),
      'wisdom': forms.NumberInput(attrs={'class': 'form-input'}),
      'raw_power': forms.NumberInput(attrs={'class': 'form-input'}),
      'combat_skills': forms.NumberInput(attrs={'class': 'form-input'}),
      'durability': forms.NumberInput(attrs={'class': 'form-input'}),
      'intelligence': forms.NumberInput(attrs={'class': 'form-input'}),
      'agility': forms.NumberInput(attrs={'class': 'form-input'}),
    }

class ImageForm(forms.ModelForm):
  class Meta:
    model = SuperheroImage
    fields = ['image']
    widgets = {
      'image': forms.FileInput(attrs={'class':'form-input'}),
    }

class CommentForm(forms.ModelForm):
    class Meta:
      model = Comment
      fields = ['text']
      widgets = {
          'text': forms.Textarea(attrs={'class': 'form-textarea'})
        }