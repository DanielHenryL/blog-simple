from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from .models import Post , User, Comment, Like, PostView
from .forms import CommentsForm, PostForm 
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


    def post(self, *args, **kwargs):
        form = CommentsForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('posts:post_detail', slug=post.slug)
        return redirect('posts:post_detail', slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form':CommentsForm()
        })
        return context


    def get_object(self, **kwargs):
        object = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
        return object
    
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
    

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'posts/post_confirm_delete.html'
    
    def get_success_url(self):
        comment = self.get_object()
        print(comment)
        post = Post.objects.get(pk=comment.post.pk)
        print(post)
        print(post.slug)
        return reverse_lazy('posts:post_detail', kwargs={'slug':post.slug})
    

def like(request, slug):
    # post = get_object_or_404(Post, slug=slug)
    post = Post.objects.get(slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)

    if like_qs.exists():
        like_qs[0].delete()
        return redirect('posts:post_detail',slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('posts:post_detail',slug=slug)