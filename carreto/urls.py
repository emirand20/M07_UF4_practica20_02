from django.urls import path

from. import views

urlpatterns = [
    path('', views.lista_carrito, name="lista_carrito"),
    path('id=<str:ct>', views.carrito_id, name="carrito_id"),
    path('crear', views.add_carrito, name='add_carrito'),
    path('modificar/<str:ct>', views.modif_carrito, name='modif_carrito'),
    path('borrar/<str:ct>', views.delete_all_carrito, name='delete_all_carrito')
]