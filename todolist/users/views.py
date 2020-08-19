from django.shortcuts import render

from django.views.generic import View, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib import messages


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        user_credentials = {
            'password': request.POST['password']
        }

        _login = request.POST['login']

        if '@' in _login and '.' in _login:
            user_credentials['email'] = _login
        else:
            user_credentials['username'] = _login

        user = authenticate(request, **user_credentials)

        if user:
            login(request, user)
            messages.success(request, f'Welcome, {user.get_username()}')
            return HttpResponseRedirect(reverse('my_todos'))
        else:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect(reverse('login'))


class LogoutView(View):
    url = 'homepage'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse(self.url))



class RegisterView(View):
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)