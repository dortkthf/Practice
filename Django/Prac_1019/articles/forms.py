from .models import Article, Comment
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content', 'pimage']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]