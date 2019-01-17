from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from .models import User
from django.contrib.auth import views
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class ProfileView(generic.DetailView):
    template_name = "users/profile.html"
    model = User

class LogoutView(views.LogoutView):
    next_page = 'core:home'#redireciona ao conseguir deslogar

class LoginView(views.LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy('common:home')
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('common:home'))
        return super(LoginView, self).get(request)

class SignupView(views.FormView):
    form_class = UserForm
    template_name = 'users/signup.html'
    model = get_user_model()
    redirect_authenticated_user = True #unido ao def get, impede que o usuario crie contas estando logado

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('core:home'))
        return super(SignupView, self).get(request)

    def form_valid(self, form):
        self.object = form.save()
        user = authenticated(username=self.object.email, password=form.cleaned_data['password'])
        auth.login(self.request, user)

        return redirect('common:home')