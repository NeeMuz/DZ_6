from django.shortcuts import render
from .models import Wish

def index(request):
    wishes = Wish.objects.all()
    return render(request, 'index.html', {'wishes': wishes})
