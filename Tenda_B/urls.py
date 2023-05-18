
from django.contrib import admin
from django.urls import path, include
from login.login import UserAPI
from rest_framework.authtoken import views
from login.views import Login, Logout
from payment.views import PagoView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('catalog.urls'))),
    path('carreto/',include(('carreto.urls'))),
    path('api/1.0/create_user', UserAPI.as_view(), name="api_create_user"),
    path('api_generate_token/',views.obtain_auth_token),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('payment/', PagoView.as_view(), name = 'payment'),

]


