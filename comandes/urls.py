from django.urls import path

from. import views

#Dins de cataleg, trobem aquestes subrutes
#Els <str:xxx> ens permeten passar parametres a les views
urlpatterns = [
    path('', views.lista_comandas, name="lista_comandas"),
    path('<str:pk>/', views.ver_comanda, name="ver_comanda"),
    path('crear/<str:carretons>/<str:user>', views.agregar_comanda, name="agregar_comanda"),
    path('borrar/<str:idC>', views.elimina_comanda, name="elimina_comanda"),
    path('modif/<str:comId>/<str:carrito>', views.comanda_modif, name="comanda_modif"),
    path('hist/<str:idC>/', views.historialComanda_user, name="historialComanda_user")
]