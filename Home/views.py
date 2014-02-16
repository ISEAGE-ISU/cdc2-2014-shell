from django.shortcuts import render
from Home.models import client

# Create your views here.
def home(request):
    return render(request, 'Home/home.html', {'NAV1': True})

def clients(request):
    return render(request, 'Home/clients.html', {'NAV2': True})

def about(request):
    return render(request, 'Home/about.html', {'NAV3': True})

def debug(request):
    client_data = client.objects.all()
    context = { 'client' : client_data }
    return render(request, 'Home/debug.html', context)