from django import forms

class PaymentForm(forms.Form):
    numero = forms.CharField()
    fecha = forms.DateField()
    cvc = forms.CharField()