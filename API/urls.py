from django.urls import path, include

from .views import ListView, DetailView, CreateView

urlpatterns = [
  path('<file_slug>/', ListView.as_view(), name='all'),
  path('<file_slug>/<int:pk>/', DetailView.as_view(), name='detail'),
  path('create/<file_slug>/', CreateView.as_view(), name='create'),

]
