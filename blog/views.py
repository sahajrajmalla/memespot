from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/home.html'
    ordering = ['-date']


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ["title", "meme_image"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Blog
    fields = ["title", "meme_image"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        else:
            return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        else:
            return False
