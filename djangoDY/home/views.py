from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    msg = 'Index page'
    return render(request, 'index.html', {'message': msg})