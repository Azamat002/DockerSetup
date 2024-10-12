from django.contrib import admin
from django.urls import path
from blog.views import post_list  # Import the view correctly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
]
