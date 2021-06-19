from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from .models import WilldoModel

# Create your views here.
class WilldoList(ListView):
    template_name = 'list.html'
    model = WilldoModel

class WilldoDetail(DetailView):
    template_name = 'detail.html'
    model = WilldoModel

class WilldoCreate(CreateView):
    template_name = 'create.html'
    model = WilldoModel
    fields = ('title', 'note', 'task_type', 'priority', 'date')
    success_url = reverse_lazy('list')

class WilldoDelete(DeleteView):
    template_name = 'delete.html'
    model = WilldoModel
    success_url = reverse_lazy('list')

class WilldoUpdate(UpdateView):
    template_name = 'update.html'
    model = WilldoModel
    fields = ('title', 'note', 'task_type', 'priority', 'date')
    success_url = reverse_lazy('list')

def descriptionfunc(request):
    template_name = 'description.html'
    return render(request, 'description.html', {})

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'success':'ユーザを登録しました。'})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザは既に登録されています。'})
    return render(request, 'signup.html', {'context':'ユーザを登録します'})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'success':'ログイン成功'})
        else:
            return render(request, 'login.html', {'error':'ログイン失敗'})
    return render(request, 'login.html', {'context':'ログインして下さい'})