Representa la interacción del jugador con el programa.
Permite asociar eventos de pulsación de teclas a métodos.

# controller.Controller #

  * **controller.Controller(_character_)**
> > Recibe el objeto del personaje a controlar.
    * **controlller.Controller.update(_keys, collisions=None_)**
> > > Realiza las acciones oportunas.
> > > Recibe las teclas del teclado que se encuentran pulsadas, en el formato devuelto por el método [pygame.key.get\_pressed](http://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) del módulo pygame.
    * **controller.Controller.bindKey(_key, action_)**
> > > Asocia una tecla a un método.
    * **controller.Controller.unbindKey(_key_)**
> > > Elimina una relación establecida con bindKey.
> > > Devuelve la referencia a la función que había asignada a la tecla eliminada.
> > > Devuelve None si la tecla no se encontraba asignada.
    * **controller.Controller.goUp()**
> > > Mueve al personaje hacia arriba.
    * **controller.Controller.goDown()**
> > > Mueve al personaje hacia abajo.
    * **controller.Controller.goLeft()**
> > > Mueve al personaje hacia la izquierda.
    * **controller.Controller.goRight()**
> > > Mueve al personaje hacia la derecha.
    * **controller.Controller.setSpeedToRun()**
> > > Hace que el personaje se mueva más rápido.