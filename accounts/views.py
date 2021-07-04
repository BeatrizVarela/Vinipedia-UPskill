from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from accounts.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from accounts.models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('homepage')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile.html
            Profile.objects.create(user=new_user)
            return render(request,
                          'accounts/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'accounts/register.html',
                  {'user_form': user_form})


@login_required
def edit(request, profile_id):

    profile = Profile.objects.get(pk=profile_id)

    if request.method == 'POST':
        user_form = UserEditForm(instance=profile.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=profile.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('accounts:profile', profile.user.id)
        else:
            messages.error(request, 'Error updating your profile.html')
    else:
        user_form = UserEditForm(instance=profile.user)
        profile_form = ProfileEditForm(instance=profile.user.profile)
    return render(request,
                  'accounts/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def profile(request, user_id):
    profile = Profile.objects.get(user_id__exact=user_id)
    return render(request,
                  'accounts/profile.html',
                  {'profile': profile.user.profile})

class ProfilesList(ListView):
    model = Profile
    template_name = 'accounts/list.html'
    context_object_name = 'profiles'


def visit_profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    return render(request,
                  'accounts/profile.html',
                  {'profile': profile})

def delete_profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    profile.delete()
    return redirect('accounts:profile_list')