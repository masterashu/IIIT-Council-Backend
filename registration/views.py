from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.


class LoginView(View):
  def get(self, request):
    return render(request, 'registration/login.html')

  def post(self, request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is None:
      error = 'Unable to login, please verify username and password.'
      return render(request, 'registration/login.html', context={'error': error})

    try:
      auth_login(request, user=user)
    except:
      error = 'Unable to login. Please try again in some time.'
      return render(request, 'registration/login.html', context={'error': error})
    if request.POST['next'] is not None:
      return redirect(to=request.POST['next'])
    return redirect(to='home')


class LogoutView(View):
  def get(self, request):
    auth_logout(request)
    return redirect(to='home')
