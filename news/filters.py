from django_filters import FilterSet, ModelChoiceFilter, DateFromToRangeFilter
from .models import Post, Author


class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'author': ['exact'],
            'dateCreated': ['gte', 'lte'],
        }
