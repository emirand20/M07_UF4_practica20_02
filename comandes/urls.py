from django.urls import path

from. import views

#Dins de cataleg, trobem aquestes subrutes
#Els <str:xxx> ens permeten passar parametres a les views
urlpatterns = [
    path('', views.veure_comandes, name="lista_comandes"),
    path('<str:pk>/', views.veure_comanda, name="una_comanda"),
    path('crear/carretons=<str:carretonsC>&user=<str:userC>', views.comanda_add, name="add_comanda"),
    path('borrar/id=<str:idC>', views.comanda_borrar, name="elimina_comanda"),
    path('modif/id=<str:comId>&carretons=<str:carrito>', views.comanda_modif, name="update_comanda"),
    path('hist/user=<str:idC>/', views.historialComanda_user, name="historialComanda_user")
]