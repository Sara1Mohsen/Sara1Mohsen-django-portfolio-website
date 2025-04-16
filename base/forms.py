from django import forms
from django.forms import ModelForm

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
  
    widgets = {
        'tags': forms.CheckboxSelectMultiple(),
    }
  
#   def __init__(self, *args, **kwargs):
#     super(PostForm, self).__init__(*args, **kwargs)
    
    