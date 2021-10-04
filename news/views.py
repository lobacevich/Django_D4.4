from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-dateCreated']
    paginate_by = 10
    form_class = NewsForm


class NewsListFilter(NewsList):
    template_name = 'news/search.html'

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news1.html'
    context_object_name = 'news'


class NewsCreate(CreateView):
    template_name = 'news/news_create.html'
    form_class = NewsForm


class NewsEdit(UpdateView):
    template_name = 'news/news_edit.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsDelete(DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
