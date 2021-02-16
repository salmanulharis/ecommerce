from django import forms
from .models import UserAccounts, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ['username', 'first_name', 'phone']

class EditForm(UserChangeForm):
    class Meta:
        model = UserAccounts
        fields = ['username', 'first_name']
    