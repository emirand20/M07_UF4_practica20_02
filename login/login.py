from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.views.generic.edit import FormView
from .forms import UserCreationForm
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

class UserAPI(FormView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('catalog:lista_productos')

    def form_valid(self, form):
        serializer = UserSerializer(data=form.cleaned_data)
        if serializer.is_valid():
            user = serializer.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


