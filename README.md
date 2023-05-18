# M07_UF4_practica20
* Crear un repo, a github, de nom M07_UF4_practica20.
* Treballar amb branques!
* Cal afegir css en tots els exercicis (s’avalua).
* Afegir captura a on es demani.
* Utilitzar KANBAN de github.
* Es realitza l’entrega del document amb l’enllaç al github.	
* Posar els noms i cognoms a la taula.
* L’entrega de la pràctica és necessària per a que el professorat sigui conscient dels coneixements adquirits per part de l’alumnat. Cal fer, mínim, un commit els dimarts i un commit els dijous en horari de M7. (Es revisaran commits)
* L’entrega es realitza segons el classroom.
* Cal fer una presentació d’aquesta pràctica i defensar-la davant dels companys.
* Defensa el 18/05. 20 minuts per grup.

# Feina Grupal
~~~
1.Crear un projecte de Django REST FRAMEWORK de nom tenda_grupX (on X es el número del grup). La BDD (la que vulgueu) ha de tindre 6 camps sense comptar id.
Aquest projecte haurà de tindre les següents 5 aplicacions:
~~~ 
~~~ 
Gestió del catàleg del producte (mínim 10 registres) (branca catalog).
~~~ 
- Afegir nous productes (commit amb missatge). 
- Actualitzar productes (commit amb missatge).
- Eliminar productes (commit amb missatge).
- Veure informació del producte (commit amb missatge).
~~~ 
Gestió del carretó de la compra (mínim, un carretó amb 4 productes) (branca cart).
~~~ 
- Afegir productes al carretó (commit amb missatge).
- Eliminar productes del carretó (commit amb missatge).
- Eliminar tot el carretó (commit amb missatge).
- Modificar quantitats (commit amb missatge).
- Botonera de compra (commit amb missatge).
~~~ 
Gestió de comandes (repartir 10 registres entre cada estat) (branca orders).
~~~ 
- Mostrar historial de compres fetes (commit amb missatge).
- Mostrar informació de carretons sense finalitzar. No cal treballar amb tokens. Si se li dona a comprar passa a històrics, si no se li dona a cap botó es queda en historial de carretons sense finalitzar i si se li dona a eliminar carretó s’elimina i no queda registre (commit amb missatge).
~~~ 
Gestió pagaments (simulat) (branca payments).
~~~ 
- Ha de tindre les opcions de; posar número de tarjeta, data caducitat i CVC.
- Si està autenticat, es consulta si les dades son correctes, i si son correctes es procedeix al pagament. Si no està autenticat, s’envia a autenticació.
- Quan es faci el pagament, es demana una autenticació (usuari i password), si està autenticat, només demana la contrasenya altra vegada (commit amb missatge).
- Una vegada feta l’autenticació, afegir la compra a històrics (gestió comandes) .Enviarà a una pàgina de compra feta amb un resum dels productes comprats. Posar botó per tornar a la pàgina principal i poder començar amb el circuit de selecció i compra.(commit amb missatge).
