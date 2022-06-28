from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
class User(AbstractUser):
    pass
    def __str__(self):
        return self.username


#post 
class Post(models.Model):
    title = models.CharField(max_length=150)       #titulo del post
    content = models.TextField()                   #contenido del post
    thumbnail = models.ImageField()                # imagen miniatura
    publish_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={
            'slug':self.slug
        })
    def get_like_url(self):
        return reverse('posts:post_like', kwargs={
            'slug':self.slug
        })
    
    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    @property
    def get_view_count(self):
        return self.postview_set.all().count()
    @property
    def get_like_count(self):
        return self.like_set.all().count()

#comentarios de nuestro post
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                          #que usuario hizo un comentario
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # comentarios que contiene el post
    timestamp = models.DateTimeField(auto_now_add=True)       #cuando se publico el comentario
    content = models.TextField()

    def __str__(self):
        return self.user.username

#visitas a nuestro post
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)   # visita que tiene el post
    timestamp = models.DateTimeField(auto_now_add=True)        #cuando se visito el post

    def __str__(self):
        return self.user.username

#Likes a nuestro post
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)   # likes que tiene el post
    
    def __str__(self):
        return self.user.username