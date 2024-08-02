from django import forms
from django.template.defaultfilters import slugify
# from huenni_blog.models import Post
from tinymce import models as tinymce_models
from .models import *



from tinymce.widgets import TinyMCE 

class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False
    
    
class PostFormular(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    title = forms.CharField(label='Beitrag - Titel',widget=forms.TextInput(attrs={'placeholder': 'Titel des Beitrages'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'comment')    
        
   