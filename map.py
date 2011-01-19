#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from xml.dom import minidom, Node
from os.path import basename
import sys

from utils import *

class Map:
	def __init__(self, name, background):
		# Nombre del fichero xml que contiene el mapa.
		self.name = name
		# Imagen de fondo.
		self.background = loadImage("data/images/backgrounds/"+background)
		# Capas del mapa.
		self.layers = []
		# Tilesets que usa el mapa.
		self.tilesets = []
		# Ancho del mapa en tiles.
		self.width = 0
		# Alto del mapa en tiles.
		self.height = 0
		# Obstáculos en el mapa.
		self.collisions = pygame.sprite.Group()

		self.loadMap()

	def loadMap(self):
		'''Carga un mapa desde un fichero xml.'''
		xmlMap = minidom.parse("data/maps/"+self.name)
		mainNode = xmlMap.childNodes[0]

		self.width = int(mainNode.attributes.get("width").value)
		self.height = int(mainNode.attributes.get("height").value)

		for i in range(len(mainNode.childNodes)):
			if mainNode.childNodes[i].nodeType == 1:
				if mainNode.childNodes[i].nodeName == "tileset":
					tileset = Tileset(mainNode.childNodes[i])
					self.tilesets.append(tileset)
				if mainNode.childNodes[i].nodeName == "layer":
					layer = Layer(mainNode.childNodes[i])
					self.layers.append(layer)
					if layer.name == 'Collisions': self.collisions = layer.getCollisions()

	def drawCollisions(self, screen):
		'''Dibuja en el mapa los tiles de colisión.'''
		self.collisions.draw(screen)

	def drawBackground(self, screen):
		screen.blit(self.background, (0,0))

	def drawFloor(self, screen):
		self.layers[0].drawLayer(screen, self.tilesets)

	def drawObstacles(self, screen):
		self.layers[1].drawLayer(screen, self.tilesets)

	def drawAir(self, screen):
		self.layers[2].drawLayer(screen, self.tilesets)

	def drawMap(self, screen):
		'''Dibuja el mapa.'''
		self.drawBackground(screen)
		self.drawFloor(screen)
		self.drawObstacles(screen)
		self.drawAir(screen)

class Tileset:
	def __init__(self, tilesetNode):
		tilewidth = tilesetNode.attributes.get("tilewidth").value
		tileheight = tilesetNode.attributes.get("tileheight").value
		firstgid = tilesetNode.attributes.get("firstgid").value
		name = tilesetNode.childNodes[1].attributes.get("source").value
		# ID del primer tile.
		self.firstgid = int(firstgid)
		# Nombre del fichero imagen del tileset.
		self.name = basename(name).encode('ascii')
		# Tamaño de un tile.
		self.tile_size = (int(tilewidth), int(tileheight))
		# Tamaño de la imagen.
		self.image_size = (0,0)
		# Tabla de tiles.
		self.table = []

		self.loadTileset()

	def loadTileset(self):
		'''Carga la tabla de tiles.'''
		image = loadImage('data/images/tilesets/'+self.name, True)
		self.image_size = image.get_size()
		for tile_x in range(0, self.image_size[0]/self.tile_size[0]):
			line = []
			self.table.append(line)
			for tile_y in range(0, self.image_size[1]/self.tile_size[1]):
				rect = (tile_x*self.tile_size[0], tile_y*self.tile_size[1], self.tile_size[0], self.tile_size[1])
				line.append(image.subsurface(rect))

	def drawTile(self, id, posx, posy, screen):
		'''Dibuja un tile en una posición dada.'''
		id = id - (self.firstgid-1)
		y = id/len(self.table)
		if id%len(self.table) == 0: y-=1
		x = (id - len(self.table)*y)-1
		screen.blit(self.table[x][y], (posx*self.tile_size[0],posy*self.tile_size[1]))
		

	def drawTileset(self, screen):
		'''Dibuja el tileset en pantalla.'''
		for x, row in enumerate(self.table):
			for y, tile in enumerate(row):
				screen.blit(tile, (x*self.tile_size[0], y*self.tile_size[1]))

class Layer:
	def __init__(self, layerNode):
		layer = decode(layerNode.childNodes[1].childNodes[0].data.replace("\n", "").replace(" ", ""))
		self.width = int(layerNode.attributes.get("width").value)
		self.height = int(layerNode.attributes.get("height").value)
		self.name = layerNode.attributes.get("name").value
		self.matrix = psplit(layer, self.width)

	def getCollisions(self):
		'''Obtiene los puntos de colisión de una capa.'''
		collisions = pygame.sprite.Group()
		for i in range(0,len(self.matrix)):
			for j in range(0,len(self.matrix[i])):
				id = self.matrix[i][j]
				if id!=0:
					rect = pygame.Rect(j*self.width, i*self.height, self.width, self.height)
					sprite = pygame.sprite.Sprite(collisions)
					sprite.image = loadImage("data/images/tile.png", True)
					sprite.rect = sprite.image.get_rect()
					sprite.rect.left = j*40
					sprite.rect.top = i*40
		return collisions

	def printLayer(self):
		'''Imprime el contenido de una capa.'''
		for row in self.matrix:
			line = ""
			for tile in row:
				line += "\t"+str(tile)
			print line

	def drawLayer(self, screen, tilesets):
		'''Dibuja una capa.'''
		for i in range(0,len(self.matrix)):
			for j in range(0,len(self.matrix[i])):
				id = self.matrix[i][j]
				if id!=0:
					for k in range(0,len(tilesets)):
						if id >= tilesets[len(tilesets)-k-1].firstgid:
							tilesets[len(tilesets)-k-1].drawTile(id, j, i, screen)
							break

def main():
	pygame.init()
	pygame.display.set_caption("Ngn Map Test")
	icon = pygame.image.load("data/images/icon.png")
	pygame.display.set_icon(icon)
	mode_flags = 0
	#mode_flags = pygame.FULLSCREEN
	#mode_flags = pygame.NOFRAME
	screen = pygame.display.set_mode((800, 600), mode_flags)
	clock = pygame.time.Clock()

	map = Map('test.tmx', 'back.jpg')

	while True:
		time = clock.tick(40)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit(0)
		map.drawMap(screen)
		pygame.display.flip()
 
if __name__ == '__main__':
	main()
