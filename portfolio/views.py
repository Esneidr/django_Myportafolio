from django.shortcuts import render
from .models import portfolio

def home(request):
    portfolios = portfolio.objects.all()
    return render(request, 'home.html', {'portfolios': portfolios})
