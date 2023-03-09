""" forms for Comment and Recipe """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ Comment Form"""
    class Meta:
        """ fields for comment form"""
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields[
            'body'
            ].label = ""


