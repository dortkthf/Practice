from .models import Imgboard
from django import forms

class ImgForm(forms.ModelForm):
    class Meta:
        model = Imgboard
        fields = ['title', 'content', 'image']