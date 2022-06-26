from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from .models import Post , User, Comment, Like, PostView
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'base.html', context)

class PostListView(ListView):
    model = Post
    tamplate_name = 'posts/post_list.html'
    context_object_name = 'posts'
    

class PostDetailView(DetailView):
    model = Post
    tamplate_name = 'posts/post_list.html'
    context_object_name = 'post'
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('posts:post_list')
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug'
    )
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug'
    )
    context_object_name = 'post'
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')
    
    
