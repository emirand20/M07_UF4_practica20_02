from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ListaProductos, name='lista_productos'),
    path('productos/<int:pk>/', views.DetalleProducto, name='detalle_producto'),
    path('productos/agregar/', views.AgregarProducto, name='agregar_producto'),
    path('productos/<int:pk>/actualizar/', views.ActualizarProducto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar/', views.EliminarProducto, name='eliminar_producto'),
]
