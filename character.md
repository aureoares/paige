Representa a los personajes del juego, ya sean jugadores o no jugadores.

# character.Character #

  * **character.Character(_charaset, width, height_)**
> > Recibe el nombre del fichero que contiene las imágenes del personaje y el ancho y alto de cada una. La imagen del personaje puede ser de cualquier tamaño, pero debe constar de 4 filas de imágenes correspondientes a las diferentes posiciones (moviéndose hacia abajo, izquierda, derecha y arriba). Cada fila debe ser una secuencia de 4 imágenes que se corresponden con la animación del personaje moviéndose en esa dirección.
    * **character.Character.loadCharaset(_charaset_)**
> > > Carga la tabla de imágenes del personaje a partir de un fichero de imagen.
    * **character.Character.update(_dir='', collisions=None_)**
> > > Actualiza el estado del personaje. Controla la animación y el movimiento. El parámetro dir es el que se le pasará al método move.
    * **character.Character.collide(_rect, collisions_)**
> > > Comprueba si un rectángulo colisiona con cualquier otro de un grupo de sprites.
    * **character.Character.move(_dir_)**
> > > Mueve al personaje.
> > > El parámetro dir puede ser cualquier cadena e indica la dirección en la que se debe mover al personaje.
> > > Sólo se tendrá en cuenta si la cadena contiene o no los caracteres 'u' (up), 'd' (down), 'l' (left) y 'r' (right).
> > > Se pueden utilizar combinaciones para realizar movimientos diagonales.
    * **character.Character.setSpeed(_speed_)**
> > > Establece la velocidad de movimiento del personaje.
> > > La velocidad debe ser un número entre 0 y 1.
    * **character.Character.drawCharacter(_screen_)**
> > > Dibuja el personaje en pantalla y su nombre encima.