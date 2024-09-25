from django.shortcuts import render
# Basic Class Base Views
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import ListView
# Crud Class Base Views
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# import models

from .models import Post


class HomePage(TemplateView):
    """
    A simple CBV to render a template.
    Here is there is no context so it is just to load a html template 
    
    This is good for pages that have no changing data, and will remain static. 
    """
    template_name = 'blog/index.html'


class BlogList(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name= 'posts'


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'posts' # this is the context name within the template so {% for post in posts %}