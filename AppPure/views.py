#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .forms import AddForm
from .models import Usr

def index(request):
    return render(request, 'AppPure/index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def temp(request):
    return render(request, 'AppPure/temp.html')

def time(request):
    return render(request, 'AppPure/time.html')

def login(request):
    if request.method == 'POST':# 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            try:
                data = Usr.objects.get(username=request.POST['username'])
            except:
                return render(request, 'AppPure/login.html')
            if data.passwd == request.POST['password']:
                return render(request, 'AppPure/index.html')
            else:
                return render(request, 'AppPure/login.html')
        else:
            return render(request, 'AppPure/login.html')
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'AppPure/login.html')
