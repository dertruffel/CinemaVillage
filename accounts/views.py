from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import make_password

from .models import *
from .forms import CreateUserForm, EditUserForm


# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('index')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def userPanel(request):
    return render(request, 'accounts/userpanel.html')


def userEdit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserForm(request.POST)
            if form.is_valid():
                usr = request.user
                newpassword = form.cleaned_data['newpassword1'],
                messages.info(request, newpassword[0])
                messages.info(request, str(newpassword[0]))
                usr.set_password(newpassword[0])
                usr.save()
                messages.success(request, 'Success')
                return HttpResponseRedirect(reverse('index'))

            else:
                messages.info(request, 'Form invalid')
                return render(request, 'accounts/edit.html')
        else:
            form = EditUserForm()
        context = {'form': form}
        return render(request, 'accounts/edit.html', context)
    else:
        return redirect('login')

