from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import  UserRegistrationForm,  ProfileEditForm, UserEditForm,User
from .models import Profile

# Create your views here.
def register(request):
    if request.method!="POST":
        form=UserRegistrationForm()
    else:
        form=UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(form.cleaned_data['password'])

            new_user=form.save()
            Profile.objects.create(user=new_user)
            login(request,new_user)

            return render(request,'users/register_done.html',
                          {'new_user': new_user})
    context={'form':form,}

    return render(request,'users/register.html', context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                   data=request.POST,
                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('star:home')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/register_done1.html',
                  {'user_form': user_form, 'profile_form': profile_form})
