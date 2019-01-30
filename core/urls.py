from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('amend/',views.shift_amend_view, name="shift_amend_view"),
    path('shift/', views.shift, name="shift"),
    path('display_shift/', views.display_shift, name="display_shift"),
    path('', views.index, name="index"),
]
