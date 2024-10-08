import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import PotionForm
from main.models import Potion

@login_required(login_url='/login')
def show_main(request):
    potions = Potion.objects.filter(user=request.user)
    
    last_login = request.COOKIES.get('last_login')
    if last_login is None:
        last_login = 'This is your first time here!'

    context = {
        'app' : 'Brew-ba-boo',
        'name': request.user.username,
        'class': 'PBP B',
        'potions' : potions,
        'last_login': last_login,
    }

    return render(request, "main.html", context)

def create_potion(request):
    form = PotionForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        potion = form.save(commit=False)
        potion.user = request.user
        potion.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_potion.html", context)

def show_xml(request):
    data = Potion.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Potion.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Potion.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Potion.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_potion(request, id):
    potion = Potion.objects.get(pk = id)
    form = PotionForm(request.POST or None, instance=potion)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_potion.html", context)

def delete_potion(request, id):
    potion = Potion.objects.get(pk = id)
    potion.delete()
    return HttpResponseRedirect(reverse('main:show_main'))