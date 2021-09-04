from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def index(request):
    return render(request, 'news.html')


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-dateCreated']


class NewsDetail(DetailView):
    model = Post
    template_name = 'news1.html'
    context_object_name = 'news1'
