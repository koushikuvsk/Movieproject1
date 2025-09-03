from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def ext(request):
    return render(request, 'ext.html')


def movies(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movies/')
    else:
        form = MovieForm()

    
    query = request.GET.get('search')
    if query:
        movie_list = Movie.objects.filter(moviename__icontains=query)
    else:
        movie_list = Movie.objects.all()

    return render(request, 'movies.html', {'form': form, 'movies': movie_list})

def movies(request):
    movies = Movie.objects.all()
    form = MovieForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('movies')
    return render(request, 'movies.html', {'form': form, 'movies': movies})

# ✅ Add these two views below it:
def update_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    form = MovieForm(request.POST or None, instance=movie)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('movies')
    return render(request, 'update_movie.html', {'form': form})

def delete_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        movie.delete()
        return redirect('movies')
    return render(request, 'confirm_delete.html', {'movie': movie})



@login_required(login_url='login')
def user_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        movies = Movie.objects.filter(moviename__icontains=search_query)
    else:
        movies = Movie.objects.all()
    return render(request, 'user.html', {'movies': movies})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    

def movie_register(request):
    movies = Movie.objects.all()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_register')  # Change if your URL name is different
    else:
        form = MovieForm()

    return render(request, 'movie_register.html', {'form': form, 'movies': movies})

