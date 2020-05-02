from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView, 
    ZenoItemListView, 
    ZenoCreateView
)
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('home/', PostListView.as_view(), name='home'),

    path('zenohome/', ZenoItemListView.as_view(), name='zeno-home'),
    path('zeno/new/', ZenoCreateView.as_view(), name='zeno-create'),
    path('searchbyid/', views.searchbyid, name='zeno-search'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='zeno-about'),
]
