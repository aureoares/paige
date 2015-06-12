Los mapas están basados en tiles y se dividen en 3 capas que se dibujan una encima de otra, más una imagen de fondo y una serie de zonas de colisión.

Para cargar la información de los mapas se utilizan en principio ficheros generados por la herramienta [Tiled](http://www.mapeditor.org/). El tamaño de los tiles puede ser cualquiera y no tienen por qué ser cuadrados.

# map.Map #

  * **map.Map(_name, background_)**
> > Recibe el nombre del fichero que contiene los datos del mapa y el nombre del fichero que contiene la imagen de fondo.
> > Carga automáticamente los tilesets y las capas del mapa.
    * **map.Map.loadMap()**
> > > Carga un mapa desde un fichero xml.
    * **map.Map.drawBackground(screen)**
> > > Dibuja la imagen de fondo en la pantalla.
    * **map.Map.drawFloor(_screen_)**
> > > Dibuja la capa más baja del mapa.
    * **map.Map.drawObstacles(_screen_)**
> > > Dibuja la capa intermedia del mapa.
    * **map.Map.drawAir(_screen_)**
> > > Dibuja la capa más alta del mapa.
    * **map.Map.drawMap(_screen_)**
> > > Dibuja el fondo y las capas del mapa.
    * **map.Map.drawCollisions(_screen_)**
> > > Dibuja en el mapa las zonas de colisión. En principio sólo se utiliza para hacerlas visibles durante las pruebas.

# map.Tileset #

  * **map.Tileset(_tilesetNode_)**

> > Recibe el nodo xml que contiene la información del tileset y lo carga.
    * **map.Tileset.loadTileset()**
> > > Carga la tabla de tiles.
    * **map.Tileset.drawTile(_id, posx, posy, screen_)**
> > > Dibuja un tile en una posición dada.
    * **map.Tileset.drawTileset(_screen_)**
> > > Dibuja todos los tiles del tileset, recomponiendo la imagen en pantalla. En principio se utiliza únicamente en pruebas.

# map.Layer #

  * **map.Layer(_layerNode_)**

> > Recibe el nodo xml que contiene la información de la capa y la carga.
    * **map.Layer.printLayer()**
> > > Muestra por la salida estándar la información de una capa. En principio sólo se utiliza para realizar pruebas, aunque no se descarta utilizarla más adelante para juegos basados en texto.
    * **map.Layer.drawLayer(_screen, tilesets_)**
> > > Dibuja la capa en pantalla, basándose en un conjunto de tilesets.
    * **map.Layer.getCollisions()**
> > > Crea una lista de zonas de colisión a partir de las zonas dibujadas en una capa.