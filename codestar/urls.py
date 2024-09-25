from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), 
    # This includes all of the paths from blog/urls.py 
    # and the root within the address bar will be "www.example.com/" "www.example.com"
]
