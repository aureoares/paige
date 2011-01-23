#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame

import map, character, player

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

	m = map.Map('test.tmx', 'back.jpg')
	p = player.Player('chara.png', 64, 64, 'My Hero')

	while True:
		time = clock.tick(40)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit(0)
		keys = pygame.key.get_pressed()
		p.update(keys)
		m.drawMap(screen)
		p.character.drawCharacter(screen)
		pygame.display.flip()

if __name__ == '__main__':
    main()
