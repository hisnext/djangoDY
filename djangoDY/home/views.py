from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    msg = 'Index page'
    renderUrl = render(request, 'index.html', {'message': msg}) 
    if request.path == '/single.html':
        renderUrl = render(request, 'single.html', {'message': msg})
    return renderUrl 
