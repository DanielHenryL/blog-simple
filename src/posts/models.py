from django.db import models

#post 
class Post(models.Model):
    title = models.CharField(max_length=150)       #titulo del post
    content = models.TextField()                   #contenido del post
    thumbnail = models.ImageField()                # imagen miniatura
    publish_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

#comentarios de nuestro post
class Comment(models.Model):
    # user = models.ForeignKey(User)                          #que usuario hizo un comentario
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # comentarios que contiene el post
    timestamp = models.DateTimeField(auto_now_add=True)       #cuando se publico el comentario
    content = models.TextField()

    def __str__(self):
        return self.user.username

#visitas a nuestro post
class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)   # visita que tiene el post
    timestamp = models.DateTimeField(auto_now_add=True)        #cuando se visito el post

    def __str__(self):
        return self.user.username

#Likes a nuestro post
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)   # likes que tiene el post
    
    def __str__(self):
        return self.user.username