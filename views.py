from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post,Comment,Category,PostCategory,Author

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = '-date_posted'
    template_name = 'post_list.html'
    paginate_by = 10

class PostArticle(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'
