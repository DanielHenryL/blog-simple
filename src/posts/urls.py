from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,like,CommentDeleteView

app_name='posts'

urlpatterns = [
    path('',PostListView.as_view(), name='post_list'),
    path('create/',PostCreateView.as_view(), name='post_create'),
    path('<slug>/',PostDetailView.as_view(), name='post_detail'),
    path('<slug>/update/',PostUpdateView.as_view(), name='post_update'),
    path('<slug>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/delete/comments/',CommentDeleteView.as_view(), name='post_delete_comment'),
    path('like/<slug>/',like, name='post_like'),
]