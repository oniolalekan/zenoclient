from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, ZenoItem
import requests


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'zeno/home.html', context)




class ZenoItemListView(LoginRequiredMixin, ListView):    

    model = ZenoItem
    template_name = 'zeno/zenoitem_listview.html'  # <app>/<model>_<viewtype>.html
    
    def get_context_data(self, **kwargs):
        response = requests.get('http://127.0.0.1:7000/zenos')
        zenodata = response.json()
        context = super().get_context_data(**kwargs)
        context['zenos'] = zenodata 
        return context


def searchbyid(request):
    zeno = {}
    if 'zenoid' in request.GET:
        zenoid = request.GET['zenoid']
        url = f"http://127.0.0.1:7000/zenos/{zenoid}"  
        response = requests.get(url)
        zeno = response.json()
    return render(request, 'zeno/zenobyid.html', {'zeno': zeno})


class ZenoCreateView(LoginRequiredMixin, CreateView):
    model = ZenoItem
    fields = ['zenoid', 'timestamp', 'temperature', 'duration']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'zeno/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'zeno/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'zeno/about.html', {'title': 'About'})
