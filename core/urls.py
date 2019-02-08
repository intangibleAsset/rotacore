from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('amend/',views.shift_amend_view, name="shift_amend_view"),
    path('shift/', views.shift, name="shift"),
    path('display_shift/', views.display_shift, name="display_shift"),
    path('add_employee_rota/', views.add_employee_rota, name="add_employee_rota"),
    path('', views.index, name="index"),
]
