from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome To Home Page</h1>')
    return render(request, 'home.html', {'name': "Isabela Osorio Botero"})
def about(request):
    #return HttpResponse('<h1>Welcome To Home Page</h1>')
    return render(request, 'home.html', {'name': "Isabela Osorio Botero"})