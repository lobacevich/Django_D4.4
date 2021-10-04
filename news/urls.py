from django.urls import path
from .views import NewsList, NewsDetail, NewsListFilter, NewsCreate, NewsEdit, NewsDelete

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>/', NewsDetail.as_view()),
    path('search/', NewsListFilter.as_view()),
    path('add/', NewsCreate.as_view()),
    path('<int:pk>/edit/', NewsEdit.as_view()),
    path('<int:pk>/delete/', NewsDelete.as_view()),
]