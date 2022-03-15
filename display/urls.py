from django.urls import path

from . import views
from .views import HomeView, TicketView, buyTicket, HomeDetail, LikeView,SearchView

urlpatterns = [
    #path('', views.index, name='index'),
    path('', HomeView.as_view(), name='index'),
    path('event/<slug:pk>/', HomeDetail.as_view(), name='detail'),
    path('tickets/', TicketView.as_view(), name='history'),
    path("event/<int:pk>", buyTicket, name='buyTicket'),
    path("like/<int:pk>", LikeView, name='likeEvent'),
    path('search/', SearchView.as_view(), name='search'),

]