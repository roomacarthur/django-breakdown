from django.urls import path
from .views import HomePage, BlogList, BlogDetail

urlpatterns = [
    # below both paths render the same template for examples.
    path('', HomePage.as_view(), name="home"),  # this will be the root url, so still "www.example.com/"
    path('home/', HomePage.as_view(), name="home1"),  # this will be the root url, so still "www.example.com/home/"
    path('blog/', BlogList.as_view(), name="blog-list"),
    path('blog/<slug:slug>/', BlogDetail.as_view(), name="blog-detail"),
]