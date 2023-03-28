""" forms for Comment and Recipe """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post




class RecipeForm(forms.ModelForm):
    """ Recipe Form """
    class Meta:
        """ fields for recipe form"""
        model = Post
        fields = ('title', 'description', 'ingredients',
                  'preparation_steps', 'image')

        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'preparation_steps': SummernoteWidget(),
        }

  
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields[
            'image'
            ].label = "Upload an image here"
     

class CommentForm(forms.ModelForm):
    """ Comment Form"""
    class Meta:
        """ fields for comment form"""
        model = Comment
        fields = ('body',)
    
 

 


