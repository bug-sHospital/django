from django.shortcuts import render


def home(request):
    return render(request, 'web/home.html')


def profile(request):
    return render(request, 'web/profile.html')