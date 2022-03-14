from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Event, Ticket
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.


class HomeView(ListView):
    model = Event
    template_name = 'display/_list.html'


def buyTicket(request, pk):
    if request.user.is_authenticated:
        ticket = Ticket()
        event = get_object_or_404(Event, id=request.POST.get('event_id'))
        ticket.event = event
        ticket.owner = request.user
        ticket.cost = event.cost
        ticket.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return redirect('accounts/login')


class HomeDetail(DetailView):
    model = Event
    template_name = 'display/_detail.html'

    def get_context_data(self, **kwargs):
        x = get_object_or_404(Event, id=self.kwargs['pk'])
        total_likes = x.total_likes()
        context = super(HomeDetail, self).get_context_data()
        context["total_likes"] = total_likes
        return context


class TicketView(ListView):
    model = Ticket
    template_name = 'display/_history.html'


def LikeView(request, pk):
    event = get_object_or_404(Event, id=request.POST.get('event_id2'))
    event.like.add(request.user)
    return HttpResponseRedirect(reverse('detail',args=[str(pk)]))
