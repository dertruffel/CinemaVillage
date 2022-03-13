from django.urls import path

from . import views
from .views import HomeView

urlpatterns = [
    #path('', views.index, name='index'),
    path('', HomeView.as_view(), name='index'),

]