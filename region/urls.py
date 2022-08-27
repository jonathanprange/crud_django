from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegionsCollection.as_view()),
    path('', views.RegionsDetail.as_view()),
]
