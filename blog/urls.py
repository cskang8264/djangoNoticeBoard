from django.urls import path
from . import views

urlpatterns = [
    path('', views.layout, name='layout'),
    path('blog/<int:pk>/edit/', views.edit, name='edit'),
    path('blog/<int:pk>/home/', views.home, name='home'),
    path('blog/new/', views.new, name='new'),
    path('blog/create/', views.create, name='create'),
    path('blog/newblog/', views.blogform, name='newblog'),
    path('blog/<int:pk>/remove/', views.remove, name='remove'),
    path('blog/textlist/', views.textlist, name='textlist'),
    
]
