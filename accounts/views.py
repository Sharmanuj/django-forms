from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


class Register(LoginRequiredMixin, View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'accounts/reg_form.html', {'form': form})

    def post(self,request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('home:home'))
        return render(request, 'accounts/reg_form.html', {'form': form})


class View_profile (LoginRequiredMixin,View):
    def get(self,request, pk=None):
        if pk:
            user = User.objects.get(pk=pk)
        else:
            user = request.user
        args = {'user': user}
        return render(request, 'accounts/profile.html', args)


class Edit_profile(LoginRequiredMixin, View):
    def get(self,request):
        form = EditProfileForm()
        return render(request, 'accounts/edit_profile.html', {'form': form})
    def post(self,request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:view_profile'))
        return render(request, 'accounts/edit_profile.html', {'form': form})



class Change_password(LoginRequiredMixin,View):
    def get(self,request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/change_password.html', {'form': form})

    def post(self,request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.POST, user = request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect(reverse('accounts:View_profile'))
        return render(request, 'accounts/change_password.html', {'form': form})
