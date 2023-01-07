from django.contrib import admin
from django.urls import path

from ads.views.ad import AdsDetailView, AdListCreateView

urlpatterns = [
    path('', AdListCreateView.as_view()),
    path('<int:pk>', AdsDetailView.as_view())
]