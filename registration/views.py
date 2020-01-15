from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from registration.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode as b64_encode
from mailgun.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        email, password = request.POST['email'], request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is None:
            error = 'Unable to login, please verify username and password.'
            return render(request, 'registration/login.html', context={'error': error})

        try:
            auth_login(request, user=user)
        except:
            error = 'Unable to login. Please try again in some time.'
            return render(request, 'registration/login.html', context={'error': error})
        if request.POST.get('next', None) is not None:
            return redirect(to=request.POST['next'])
        return redirect(to='home_page')


class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect(to='home')


class PasswordChangeView(LoginRequiredMixin, View):
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


class PasswordResetView(View):
    def get(self, request):
        return render(request, 'registration/prf.html')


class PasswordResetDoneView(View):
    def post(self, request):
        dtg = default_token_generator
        try:
            email = request.POST['email']
        except KeyError as e:
            error = 'Enter email id.'
            return render(request, 'registration/password_reset_form.html', context={'error': error})
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            error = 'No account found with that Email-id.'
            return render(request, 'registration/password_reset_form.html', context={'error': error})
        token = dtg.make_token(user)
        uidb64 = b64_encode(bytes(str(user.pk).encode()))
        context = {
            'email': user.email,
            'protocol': 'http',
            'domain': settings.DOMAIN,
            'uid': uidb64,
            'token': token,
            'name': user.first_name
        }
        send_mail("Password Reset", render_to_string('registration/password_reset_mail.html', context=context),
                  [user.email], 'donotreply@example.com')
        return render(request, 'registration/password_reset_done.html')


class PasswordResetConfirmView(View):
    def get(self, request, uidb64, token):

        pass


class PasswordResetCompleteView(View):
    def post(self, request):
        pass