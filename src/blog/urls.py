from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name='home'),
    path('posts/',include('posts.urls',namespace='posts')),
    path('accounts/', include('allauth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
