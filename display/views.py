from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Event
# Create your views here.


#def index(request):
    #return HttpResponse("Index")
#    return render(request,template_name='display/base.html')


class HomeView(ListView):
    model = Event
    template_name = 'display/base.html'
