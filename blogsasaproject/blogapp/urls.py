from django.contrib import admin
from django.urls import path
from .views import Home, Register, SaveJob, PostView, CategoryView, SearchResultsView, save_form, get_queryset, \
     save_job, MyFormView, save_jobpost

urlpatterns = [
    path('', get_queryset, name="home"),
    #path('/post', Post, name="post"),
    path('register/', save_form, name="register"),
    #path('post/', AddPost.as_view(), name="post"),
    #path('register/', Register.as_view(), name="register"),
    path('post/', save_jobpost, name="post"),
    path('job/<pk>', PostView, name="postdetail"),
    path('category/<str:cats>', CategoryView, name="category"),
    #path('', SearchResultsView.as_view(), name='home'),
]