from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.form import RegisterUser


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been successfully created for {username} you can log in!')
            return redirect('login-page')
    else:
        form = RegisterUser()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')