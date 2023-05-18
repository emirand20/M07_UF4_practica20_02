from django.shortcuts import render
from django.shortcuts import render, redirect
from .serializers import PagoSerializer
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Pago
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import PaymentForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

class PagoView(FormView):
    template_name = 'payment.html'
    form_class = PaymentForm
    success_url = '/login'

   

    def form_valid(self, form):
        serializer = PagoSerializer(data=form.cleaned_data)

        if serializer.is_valid():
            @method_decorator(login_required)
            def dispatch(self, request, *args, **kwargs):
                return super().dispatch(request, *args, **kwargs)
            user = serializer.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)
            