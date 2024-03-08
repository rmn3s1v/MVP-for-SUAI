from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    logout(request)
    return render(request, 'main_page/index.html')
