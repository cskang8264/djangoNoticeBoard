from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm, CommentForm
from .models import Blog, Comment

# Create your views here.


def layout(request):
    return render(request, 'blog/layout.html')

# def home(request):
#     blogs = Blog.objects
#     return render(request, 'blog/home.html', {'blogs': blogs})


def new(request):
    return render(request, 'blog/new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/home/')


def createComment(request):
    comment = Comment()
    comment.comment_text = request.GET['comment_text']
    comment.save()
    return redirect('/blog/home/')


def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():  # 유효성검사
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('textlist')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'blog/new.html', {'form': form})


        

def edit(request ,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return blogform(request, blog)

def remove(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('textlist')



def textlist(request):
    blogs = Blog.objects
    return render(request, 'blog/textlist.html',{'blogs': blogs})

def home(request, blog_id, comment=None):
    blogs = get_object_or_404(Blog, id=blog_id)
    if request.method =='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():   #유효성검사
            comment = form.save(commit=False)
            comment.blog =blogs
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect('home', blog_id)       
    else:
        form = CommentForm(instance=comment)
        return render(request, 'blog/home.html', {'blogs':blogs, 'form': form})


def commentedit(request ,blog_id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return home(request, blog_id, comment)

def commentremove(request, blog_id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('home', blog_id)