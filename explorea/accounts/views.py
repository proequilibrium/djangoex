from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, update_session_auth_hash

from .forms import RegisterForm, EditProfileForm

def profile(request):

    return render(request, 'accounts/profile.html')

def register(request):

    if request.method == 'POST':
        import pdb; pdb.set_trace()
        form = RegisterForm(request.POST)

        if form.is_valid():

            User = get_user_model()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password1')

            u = User(username=username,
                     email=email,
                     first_name=first_name,
                     last_name=last_name)
            u.set_password(password)
            u.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('profile')

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form} )

def edit_profile(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            return redirect('profile')

    form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form} )

def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/accounts/profile/')

    form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
