from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import PotionForm
from main.models import Potion

def show_main(request):
    potions = Potion.objects.all()
    
    context = {
        'app' : 'Brew-ba-boo',
        'name': 'Najwa Zarifa',
        'class': 'PBP B',
        'potions' : potions
    }

    return render(request, "main.html", context)

def create_potion(request):
    form = PotionForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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