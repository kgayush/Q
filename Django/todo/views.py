from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .models import ToDo
from .forms import MyForm


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "todo/index.html",{
        "todo_list": ToDo.objects.all()
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "todo/login.html", {
                "message": "Invalid credentials! Please login again."
            })
    else:
        return render(request, "todo/login.html")

def logout_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        logout(request)
        return render(request, "todo/logout.html")

def add_todo(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = MyForm()
    return render(request, "todo/add_todo.html", {
        "form": form
    })

def update(request, id): 
    todo = ToDo.objects.get(pk=id)
    form = MyForm(request.POST, instance=todo)
    title = todo.title
    desc = todo.desc
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'todo/add_todo.html',{
        "title": title,
        "desc": desc
    })

def delete_todo(request, id):
    ToDo.objects.get(pk=id).delete()    
    return HttpResponseRedirect(reverse("index"))

