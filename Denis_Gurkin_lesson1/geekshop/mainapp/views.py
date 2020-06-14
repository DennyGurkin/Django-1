from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def product(request):
    return render(request, 'mainapp/product.html')


def showroom(request):
    return render(request, 'mainapp/showroom.html')


def history(request):
    return render(request, 'mainapp/history.html')
