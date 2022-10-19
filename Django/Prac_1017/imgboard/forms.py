from .models import Imgboard, Comments
from django import forms

class ImgForm(forms.ModelForm):
    class Meta:
        model = Imgboard
        fields = ['title', 'content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields =['content',]