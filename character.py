#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from utils import *
from main import WIDTH, HEIGHT

class Character(pygame.sprite.Sprite):
	'''Clase base para los personajes.'''
	def __init__(self, charaset, width, height, name=''):
		pygame.sprite.Sprite.__init__(self)
		# Charaset del personaje.
		self.charaset = []
		# Ancho del personaje (no de la imagen completa, sino de un frame).
		self.width = width
		# Alto del personaje (no de la imagen completa, sino de un frame).
		self.height = height
		self.loadCharaset(charaset)
		# Frame de la animación en que se encuentra (0-3).
		self.frame = 0
		# Dirección en la que mira el personaje (0-3).
		self.direction = 0
		# Imagen actual del personaje.
		self.image = self.charaset[self.frame][self.direction]
		# Indica si realizar la animación del personaje aunque no se esté moviendo.
		self.animate = True
		# Rectángulo que representa al personaje.
		self.rect = self.image.get_rect()
		# X inicial del personaje.
		self.rect.centerx = WIDTH / 2
		# Y inicial del personaje.
		self.rect.centery = HEIGHT / 2
		# Rectángulo que representa la parte del personaje a tener en cuenta para las colisiones.
		self.rect_col = pygame.Rect(self.rect.topleft[0], (self.rect.bottomleft[1]+self.rect.topleft[1])/2, self.width, self.height/2)
		# Velocidad de movimiento del personaje.
		self.speed = 0.25
		# Direcciones en las que se puede mover.
		self.up_clear = True
		self.down_clear = True
		self.right_clear = True
		self.left_clear = True
		# Nombre del personaje.
		self.name = name
		# Velocidad de movimiento por defecto.
		self.WALK = 0.15
		# Velocidad de movimiento en carrera.
		self.RUN = 0.25

	def loadCharaset(self, charaset):
		'''Carga la tabla de imágenes del personaje.'''
		image = loadImage('data/images/charasets/'+charaset, True)
		image_size = image.get_size()
		for x in range(0, image_size[0]/self.width):
			line = []
			self.charaset.append(line)
			for y in range(0, image_size[1]/self.height):
				rect = (x*self.width, y*self.height, self.width, self.height)
				line.append(image.subsurface(rect))

	def update(self, dir='', collisions=None):
		'''Actualiza el estado del personaje.'''
		moved = self.move(dir, collisions)
		if self.animate or moved:
			if int(self.speed*4) > 0:
				self.frame += int(self.speed*4)
			else:
				self.frame += 1
			if self.frame > 39: self.frame = 0
		else:
			self.frame = 0
		self.image = self.charaset[self.frame/10][self.direction]

	def collide(self, rect, collisions):
		'''Comprueba si un rectángulo colisiona con cualquier otro de un grupo de sprites.'''
		for sprite in collisions:
			if sprite.rect.colliderect(rect): return True
		return False

	def move(self, dir, collisions):
		'''Mueve al personaje.
		El parámetro dir puede ser cualquier cadena e indica la dirección en la que se debe mover al personaje.
		Sólo se tendrá en cuenta si la cadena contiene o no los caracteres 'u' (up), 'd' (down), 'l' (left) y 'r' (right).
		Se pueden utilizar combinaciones para realizar movimientos diagonales.'''
		moved = False
		if self.speed > 0:
			# Si len(dir)>1, entonces vamos a hacer un movimiento diagonal.
			# No podemos mover la distancia normal en ambas direcciones porque el personaje iría más rápido de lo normal.
			# La siguiente corrección es una aproximación utilizando el teorema de Pitágoras.
			if len(dir) > 1: dist = self.speed * 21.213203436
			else: dist = self.speed * 30
			if self.up_clear:
				if 'u' in dir:
					self.direction = 3
					newRect = self.rect_col.copy()
					newRect.centery -= dist
					if not self.collide(newRect, collisions):
						self.rect_col = newRect.copy()
						self.rect.centery -=dist
						moved = True
			if self.down_clear:
				if 'd' in dir:
					self.direction = 0
					newRect = self.rect_col.copy()
					newRect.centery += dist
					if not self.collide(newRect, collisions):
						self.rect_col = newRect.copy()
						self.rect.centery +=dist
						moved = True
			if self.left_clear:
				if 'l' in dir:
					self.direction = 1
					newRect = self.rect_col.copy()
					newRect.centerx -= dist
					if not self.collide(newRect, collisions):
						self.rect_col = newRect.copy()
						self.rect.centerx -=dist
						moved = True
			if self.right_clear:
				if 'r' in dir:
					self.direction = 2
					newRect = self.rect_col.copy()
					newRect.centerx += dist
					if not self.collide(newRect, collisions):
						self.rect_col = newRect.copy()
						self.rect.centerx +=dist
						moved = True
		return moved

	def setSpeed(self, speed):
		'''Establece la velocidad de movimiento del personaje.
		La velocidad debe ser un número entre 0 y 1.'''
		if speed>=0 and speed<=1: self.speed = speed
		else: print "Velocidad incorrecta para el personaje '" + self.name + "'."

	def drawCharacter(self, screen):
		'''Dibuja el personaje en pantalla y su nombre encima.'''
		t, t_rect = loadText(self.name, (self.rect.topleft[0]+self.rect.topright[0])/2, self.rect.topleft[1]-5, size=10, center=True)[0]
		screen.blit(t, t_rect)
		screen.blit(self.image, self.rect)
