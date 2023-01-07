from django.contrib import admin
from django.urls import path

from ads.views.cat import CategoriesDetailView, CatListCreateView


urlpatterns = [
    path('', CatListCreateView.as_view()),
    path('<int:pk>', CategoriesDetailView.as_view())
]