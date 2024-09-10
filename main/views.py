from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'Brew-ba-boo',
        'name': 'Najwa Zarifa',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)