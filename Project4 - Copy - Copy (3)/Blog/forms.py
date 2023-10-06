from django import forms
from django.forms import ModelForm
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content']
        widgets = { 'title': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'content': forms.TextInput(attrs={ 'class': 'form-control' }),
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title)<10:
            raise ValidationError ('The title must have at least 10 characters')
        return title
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content)<20:
            raise ValidationError('The content must have at least 20 characters')
        return content
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']