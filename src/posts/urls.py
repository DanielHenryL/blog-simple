from django.urls import path
from .views import listView

app_name='posts'

urlpatterns = [
    path('',listView.as_view(), name='post_list')
]