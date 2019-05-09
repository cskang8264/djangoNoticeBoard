from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        # model = Blog
        # title = forms.CharField(widget=forms.TextInput(attrs={
        #     'placeholder': '제목',
        #     'class': 'form-control',
        #     'id': 'exampleFormControlInput1'}
        #     ))

        # body = forms.Textarea(widget=forms.Textarea(attrs={
        #     'class': 'form-control',
        #     'id': 'exampleFormControlInput1'}
        #     ))
        # fields = ['title', 'body']

        model = Blog
        
        fields = ['title', 'body']
