from django.shortcuts import render


def card_collection(request):
    return render(request, 'collection.html')


def index(request):
    return render(request, 'index.html')
