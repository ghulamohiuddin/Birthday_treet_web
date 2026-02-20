from django.shortcuts import render


def home(request):
    return render(request, 'proposal/home.html')


def success(request):
    return render(request, 'proposal/success.html')
