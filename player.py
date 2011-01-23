#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.locals import *

import character

class Player():
	'''Clase para personajes controlados por jugadores.'''
	def __init__(self, charaset, width, height, name=''):
		self.character = character.Character(charaset, width, height)
		self.character.name = name
		# Velocidad de movimiento por defecto.
		self.WALK = 0.25
		# Velocidad de movimiento en carrera.
		self.RUN = 0.5
	def update(self, keys):
		'''Actualiza el estado del jugador.'''
		if keys[K_z]: self.character.setSpeed(self.RUN)
		else: self.character.setSpeed(self.WALK)
		dir = ''
		if keys[K_UP]: dir += 'u'
		elif keys[K_DOWN]: dir += 'd'
		if keys[K_LEFT]: dir += 'l'
		elif keys[K_RIGHT]: dir += 'r'
		self.character.update(dir)
