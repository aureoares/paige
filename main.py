#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

import map, character, controller
from utils import *

WIDTH = 800
HEIGHT = 600

def main():
	pygame.init()
	pygame.display.set_caption("Paige Test")
	icon = pygame.image.load("data/images/icon.png")
	pygame.display.set_icon(icon)
	mode_flags = 0
	#mode_flags = pygame.FULLSCREEN
	#mode_flags = pygame.NOFRAME
	screen = pygame.display.set_mode((WIDTH, HEIGHT), mode_flags)
	clock = pygame.time.Clock()

	# Cargamos el mapa de prueba.
	m = map.Map('test.tmx', 'back.jpg')
	# Creamos los personajes para los jugadores.
	player1 = character.Character('chara.png', 64, 64, 'My Heroe')
	player2 = character.Character('Izhal.png', 32, 48, 'My Heroine')
	player2.animate = False

	# Controles para el primer jugador.
	c1 = controller.Controller(player1)
	c1.bindKey(K_w, c1.goUp)
	c1.bindKey(K_s, c1.goDown)
	c1.bindKey(K_a, c1.goLeft)
	c1.bindKey(K_d, c1.goRight)
	c1.bindKey(K_LSHIFT, c1.setSpeedToRun)
	# Controles para el segundo jugador.
	c2 = controller.Controller(player2)
	c2.bindKey(K_UP, c2.goUp)
	c2.bindKey(K_DOWN, c2.goDown)
	c2.bindKey(K_LEFT, c2.goLeft)
	c2.bindKey(K_RIGHT, c2.goRight)
	c2.bindKey(K_RSHIFT, c2.setSpeedToRun)
	# Texto que describe los controles.
	text = "Jugador 1 :\nArriba = W\nAbajo = S\nIzquierda = A\nDerecha = D\nCorrer = Mayuscula (Shift) izquierda\n"
	text += "\nJugador 2 :\nArriba = Flecha Arriba\nAbajo = Flecha Abajo\nIzquierda = Flecha Izquierda\nDerecha = Flecha Derecha\nCorrer = Mayuscula (Shift) derecha\n"
	text += "\n\nPulsa una tecla para continuar..."

	# Bucle que muestra el texto de ayuda hasta que se pulse una tecla.
	while not pygame.event.wait().type in (QUIT, KEYDOWN):
		text_lines = loadText(text, 20, 20, size=20)
		for t, t_rect in text_lines:
			screen.blit(t, t_rect)
		pygame.display.flip()

	# Bucle principal.
	while True:
		time = clock.tick(40)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit(0)
		keys = pygame.key.get_pressed()
		# Actualizamos el estado de los controles.
		c1.update(keys, m.collisions)
		c2.update(keys, m.collisions)
		# Dibujamos todo en orden.
		m.drawFloor(screen)
		m.drawObstacles(screen)
		player1.drawCharacter(screen)
		player2.drawCharacter(screen)
		m.drawAir(screen)
		# Actualizamos la pantalla.
		pygame.display.flip()

if __name__ == '__main__':
    main()
