from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from .models import Post , User, Comment, Like, PostView
from .forms import PostForm
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
    form_class = PostForm
    model = Post
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('posts:post_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'create'
        # context.update({
        #     'view_type':'create'
        # })
        return context
    
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'posts/post_form.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'update'
        # context.update({
        #     'view_type':'update'
        # })
        return context
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('posts:post_list')
    
    
