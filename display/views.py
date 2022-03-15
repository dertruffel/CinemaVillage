from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context
from django.views.generic import ListView, DetailView

from accounts.models import User
from .models import Event, Ticket
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.


class HomeView(ListView):
    model = Event
    paginate_by = 3
    template_name = 'display/_list.html'


class SearchView(ListView):
    model = Event
    paginate_by = 3
    template_name = 'display/_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Event.objects.filter(
            title__icontains=query
        )
        return object_list


def buyTicket(request, pk, test=None):
    if request.user.is_authenticated:
        ticket = Ticket()
        if test is not None:
            event = get_object_or_404(Event, id=1)
            ticket.event = event
            ticket.owner = request.user
            ticket.cost = event.cost
            ticket.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            event = get_object_or_404(Event, id=request.POST.get('event_id'))
            ticket.event = event
            ticket.owner = request.user
            ticket.cost = event.cost
            ticket.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        return redirect('accounts/login')


def test_makeEvent(user):
    event = Event()
    event.title = 'Test event'
    event.description = 'description'
    event.image = 'media/interstellar.jpg'
    event.cost = 110
    event.author = user
    event.location = 'location'
    event.save()
    return HttpResponseRedirect(reverse('index'))


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
    paginate_by = 4
    template_name = 'display/_history.html'






def LikeView(request, pk):
    event = get_object_or_404(Event, id=request.POST.get('event_id2'))
    event.like.add(request.user)
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))
