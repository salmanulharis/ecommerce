from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.views.generic import ListView, DetailView, TemplateView
from .models import UserAccounts
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import EditForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        return redirect('/accounts/login/')

class ListUsers(ListView):
    template_name = 'accounts/list_users.html'
    model = UserAccounts
    context_object_name = 'users'

    def get_queryset(self):
        sort = self.kwargs['sort']
        if sort == 'desc':
            queryset= self.model.objects.all().order_by('-username')
        else:
            queryset= self.model.objects.all().order_by('username')
        return queryset

class DetailedUser(DetailView):
    template_name = 'accounts/detailed_user.html'
    model = UserAccounts
    context_object_name = 'user_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = UserAccounts.objects.all()
        return context

class Login(FormView):
    template_name = 'accounts/login.html'
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('username or password incorrect')

class ChangePassword(FormView):
    template_name = 'accounts/register.html'
    form_class = PasswordChangeForm

    def get(self, request):
        form = self.form_class(user= request.user)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(form.user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form':form})

class EditUser(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/register/'
    template_name = 'accounts/register.html'
    model = UserAccounts
    fields = ['username', 'first_name', 'phone']
    success_url = '/products/home/'



def logout_fn(request):
    logout(request)
    return redirect('/accounts/login/')
