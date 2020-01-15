from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'login/registration/login.html')

    def post(self, request):
        email, password = request.POST['email'], request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is None:
            error = 'Unable to login, please verify username and password.'
            return render(request, 'login/registration/login.html', context={'error': error})

        try:
            auth_login(request, user=user)
        except:
            error = 'Unable to login. Please try again in some time.'
            return render(request, 'base/login.html', context={'error': error})
        if request.POST.get('next', None) is not None:
            return redirect(to=request.POST['next'])
        return redirect(to='home_page')


class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect(to='home')


class ChangePassword(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'login/password_change.html')

    def post(self, request):
        old_pass, new_pass, conf_new_pass = request.POST['old'], request.POST['new'], request.POST['confirm_new']

        if request.user.check_password(old_pass):
            if new_pass == conf_new_pass:
                request.user.set_password(new_pass)
                return redirect(to="password_change_done")
            else:
                error = "New passwords do not match."
                return render(request, 'login/password_change.html', context={'error': error})
        else:
            error = "Old password is wrong."
            return render(request, 'login/password_change.html', context={'error': error})
