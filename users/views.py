from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from .forms import UserRegisterForm


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {
            'form': form
        })

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            messages.success(request, f"Account created for {username}")
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('main-page')
        return render(request, "users/register.html", {
            'form': form
        })


@login_required
def user_logout(request):
    username = request.user.username
    logout(request)
    messages.success(request, f"{username} was logged out successfully")
    return render(request, 'users/logout.html')
