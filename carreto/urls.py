from django.urls import path

from. import views

#Dins de cataleg, trobem aquestes subrutes
#Els <str:xxx> ens permeten passar parametres a les views
urlpatterns = [
    path('', views.lista_carrito, name="llistat"),
    path('id=<str:pk>', views.carrito_id, name="un_producte"),
    path('crear', views.add_carrito, name='crear_producto'),
    path('modificar/<str:pk>', views.modif_carrito, name='actualizar_producto'),
    '''path('borrar/<str:pk>', views.delete_all_carrito, name='eliminar_producto'),'''
]