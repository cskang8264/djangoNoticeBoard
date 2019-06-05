from django import forms
from .models import Blog, Comment, Hashtag 


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'hashtags', 'image','imageTitle', 'imageText']
        labels = {
            'title': '제  목',
            'body': '본  문',
            'hashtags': '해 시 태 그',
            'image': '이 미 지',
            'imageTitle': '이미지 이름',
            'imageText':'이미지 설명',
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]
        labels = {
            'comment_text': '댓글좀',
        }


class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ["name"]
        labels = {
            'name': '해시태그를 입력하세요',
        }



