from django.urls import path

from. import views

urlpatterns = [
    path('', views.lista_carrito, name="lista"),
    path('id=<str:pk>', views.carrito_id, name="producto"),
    path('crear', views.add_carrito, name='crear_producto'),
    path('modificar/<str:pk>', views.modif_carrito, name='actualizar_producto'),
    path('borrar/<str:pk>', views.delete_all_carrito, name='eliminar_producto')
]