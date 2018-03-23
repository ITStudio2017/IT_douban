from django import forms
from .models import Label


class BookFrom(forms.Form):
    bookname = forms.CharField(max_length=20)
    introduction = forms.CharField(max_length=500, widget=forms.Textarea)
    author = forms.CharField(max_length=30)
    #flabel = forms.ChoiceField()
    #slabel = forms.ChoiceField()
    cover = forms.ImageField()
