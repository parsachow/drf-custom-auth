from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

#included on the details page, so have to make a forms.py. not having to open a whole new form
class RegisterForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ['email', 'name',]
