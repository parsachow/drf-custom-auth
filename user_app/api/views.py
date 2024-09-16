from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.mixins import CreateModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from channels.layers import get_channel_layer

from .permissions import CustomUserOrReadOnly
from .serializers import RegistrationSerializer, CustomUserSerializer
from ..models import CustomUser


class RegisterView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
    

class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [CustomUserOrReadOnly]
    permission_classes = [IsAuthenticated]
    
# class UserDetailView(RetrieveAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [IsAuthenticated]

