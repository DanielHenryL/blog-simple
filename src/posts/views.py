from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Post
# Create your views here.


class listView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context ={
            'posts':posts,
        }
        return render(request, 'post_list.html',context)

        
# class listview(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'post_list.html'
    
