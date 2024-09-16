from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from channels.layers import get_channel_layer
from channels import layers

from .forms import RegisterForm
from .models import CustomUser
from asgiref.sync import async_to_sync


class Home(LoginRequiredMixin, ListView):
    model = CustomUser
    
    def get(self, request):
        
        users = CustomUser.objects.all()
        
        return render(request, 'home.html', {
            'users': users
        })

# def home(request):
#     return render(request, 'home.html')

class Login(LoginView):
    template_name = "login.html"
    
class Logout(LogoutView):
    success_url = reverse_lazy("login")

class Register(CreateView):
    template_name = "signup.html"
    form_class = RegisterForm
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        # Save the form and create the user
        response = super().form_valid(form)

        # Log in the user after signing up
        user = authenticate(
            email=form.cleaned_data["email"],
        )
        if user is not None:
            login(self.request, user)
        
            
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"notification",
                {
                    "type": "send_notification",
                    "notification": f"{user} has joined"
                }
            )
        # data = {
        # "type":"send_notification",
        # "message": "new user registered"
        # }
        # channel_layer = get_channel_layer()
        # (channel_layer.group_send)("notification", data)

        return response
