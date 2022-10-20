from xml.etree.ElementTree import Comment
from .models import Article, Comments
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']