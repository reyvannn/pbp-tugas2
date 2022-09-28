from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django import forms
import todolist.models as models
import datetime

class CreateTaskForm(forms.Form):
    date = forms.DateField(label="Date")
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")

@login_required(login_url='/todolist/login/')
def show_homepage(request):
    data = models.Task.objects.filter(user=request.user).order_by("date").all()
    context = {
        'list_task' : data,
        'last_login' :request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

def create_task(request: HttpRequest):
    form = CreateTaskForm()
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = models.Task(
                date=form.cleaned_data["date"],
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                user=request.user,
            )
            task.save()
            messages.success(request, "Berhasil disimpan!")
            return redirect("todolist:show_homepage")
    context = {"form": form}
    return render(request, "create-task.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_homepage"))
            response.set_cookie('last_login',
                                str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response