from django.shortcuts import render
from django.conf import settings


# Create your views here.

def index(request):
    print(settings.STATICFILES_FINDERS)
    return render(request, 'booktest/index.html')