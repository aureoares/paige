# -*- coding: utf-8 -*-

from pygame.locals import *
from pygame import event

class Controller():
	'''Representa la interacción del jugador con el programa.
	Permite asociar eventos de pulsación de teclas a métodos.'''
	def __init__(self, character):
		self.character = character
		self.keys = {}
		self.direction = ''

	def update(self, keys, collisions=None):
		'''Realiza las acciones oportunas.'''
		# Estado por defecto.
		self.character.setSpeed(self.character.WALK)
		self.direction = ''
		# Realizamos las acciones.
		for key, action in self.keys.items():
			if keys[key]:
				action()
		# Actualizamos el personaje.
		self.character.update(self.direction, collisions)

	def goUp(self):
		'''Mueve al personaje hacia arriba.'''
		self.direction += 'u'
	def goDown(self):
		'''Mueve al personaje hacia abajo.'''
		self.direction += 'd'
	def goLeft(self):
		'''Mueve al personaje hacia la izquierda.'''
		self.direction += 'l'
	def goRight(self):
		'''Mueve al personaje hacia la derecha.'''
		self.direction += 'r'

	def setSpeedToRun(self):
		'''Hace que el personaje se mueva más rápido.'''
		self.character.setSpeed(self.character.RUN)

	def bindKey(self, key, action):
		'''Asocia una tecla a un método.'''
		self.keys[key] = action

	def unbindKey(self, key):
		'''Elimina una relación establecida con bindKey.
		Devuelve la referencia a la función que había asignada a la tecla eliminada.
		Devuelve None si la tecla no se encontraba asignada.'''
		try:
			return self.keys.pop(key)
		except KeyError:
			print "La tecla " + key + " no se encontraba asignada."
			return None
