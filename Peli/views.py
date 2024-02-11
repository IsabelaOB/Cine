from django.shortcuts import render
from django.http import HttpResponse
from .models import pelicula
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome To Home Page</h1>')
    #return render(request, 'home.html', {'name': "Isabela Osorio Botero"})
    searchTerm= request.GET.get('searchpelicula')
    if searchTerm:
        peliculas = pelicula.objects.filter(title__icontains=searchTerm)
    else:
        peliculas = pelicula.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'peliculas': peliculas})
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Reemplaza 'home' con el nombre de tu vista principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Reemplaza 'home' con el nombre de tu vista principal
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
def about(request):
    #return HttpResponse('<h1>Welcome To Home Page</h1>')
    return render('<h1>Welcome to Home Page</h1>')

