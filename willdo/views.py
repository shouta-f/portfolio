from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    fields = ('title', 'note', 'task_type', 'priority', 'date', 'create_user')

    def test_func(request):  # UserPassesTestMixin
        u = User.objects.all()
        a = willdoproject.objects.all()
        print(u)
        print(a)

    success_url = reverse_lazy('list')



class WilldoDelete(DeleteView):
    template_name = 'delete.html'
    model = WilldoModel
    fields = ('create_user')
    success_url = reverse_lazy('list')

class WilldoUpdate(UpdateView):
    template_name = 'update.html'
    model = WilldoModel
    fields = ('title', 'note', 'task_type', 'priority', 'date')
    success_url = reverse_lazy('list')

def descriptionfunc(request):
    template_name = 'description.html'
    return render(request, 'description.html')

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, password)
            return redirect('list')
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
            return redirect('list')
        else:
            return render(request, 'login.html', {'error':'ログイン失敗', 'message':'ご入力頂いたUsername、Passwordが一致しておりません。'})
    return render(request, 'login.html', {'context':'ログインして下さい'})

def logoutfunc(request):
    logout(request)
    return redirect('list')
    