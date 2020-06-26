from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account have been successfully created {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        Uform = UserUpdateForm(request.POST, instance=request.user)
        Pform = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if Uform.is_valid() and Pform.is_valid():
            Uform.save()
            Pform.save()
            username = Uform.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been successfully updated', {username})
            return redirect('profile')
    else:
        Uform = UserUpdateForm(instance=request.user)
        Pform = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "Uform": Uform,
        "Pform": Pform,
    }

    return render(request, 'users/profile.html', context)
