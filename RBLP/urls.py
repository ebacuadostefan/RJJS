from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.index_gender),
]
