from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('IntDesign:services')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
