from django.urls import path
from . import views

urlpatterns = [
    path('', views.layout, name='layout'),
    path('blog/<int:blog_id>/edit/', views.edit, name='edit'),
    path('blog/<int:blog_id>/home/', views.home, name='home'),
    path('blog/new/', views.new, name='new'),
    path('blog/create/', views.create, name='create'),
    path('blog/newblog/', views.blogform, name='newblog'),
    path('blog/<int:blog_id>/remove/', views.remove, name='remove'),
    path('blog/textlist/', views.textlist, name='textlist'),
    path('blog/<int:blog_id>/commentedit/<int:pk>/', views.commentedit, name='commentedit'),
    path('blog/<int:blog_id>/commentremove/<int:pk>/', views.commentremove, name='commentremove'),  
    path('blog/hashtag/', views.hashtagform, name='hashtag'),
    path('blog/<int:hashtag_id>/search/', views.search, name='search'),
]
