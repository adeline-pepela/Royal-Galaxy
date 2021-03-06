from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django .forms import ModelForm, Textarea
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    fullname=forms.CharField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'password1','password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')  
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name',  'bio', 'prof_pic')

class UploadRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['user'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 15, 'rows': 6}),
        } 
    class Meta:
        model = Comment
        exclude = ['recipe','user']    