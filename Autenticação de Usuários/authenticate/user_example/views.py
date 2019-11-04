from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def error_404_view(request, exception):
    #data = {"name": "ThePythonDjango.com"}
    return render(request,'user_example/error_404.html', status= 404)

def error_500_view(request):
    return render(request, 'user_example/error_500.html', status=500)

def index(request):
    return render(request, 'user_example/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)
    
