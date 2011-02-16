#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import base64
import gzip
import StringIO
import pygame
from pygame.locals import *

def loadImage(filename, transparent=False):
	'''Carga una imagen'''
	try: image = pygame.image.load(filename)
	except pygame.error, message:
		raise SystemExit, message
	image = image.convert()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image

def loadText(text, x, y, color=(255, 255, 255), size=25, center=False):
	'''Carga un texto.
	Por defecto el texto comienza en las coordenadas x, y dadas.
	Si center es True, se centra el texto en las coordenadas x, y dadas.
	Devuelve una lista de tuplas (Surface, Rect), cada una correspondiente a una línea.'''
	font = pygame.font.Font("data/fonts/Abscissa.ttf", size)
	text_lines = []
	for line in text.split('\n'):
		t = font.render(line, 1, color)
		t_rect = t.get_rect()
		if center:
			t_rect.centerx = x
			t_rect.centery = y
		else:
			t_rect.topleft = (x,y)
		y += t.get_height()
		text_lines.append((t, t_rect))
	return text_lines

def decode(string):
	'''Recibe una cadena con el contenido de una capa (codificada con base64 y comprimida con gzip).
	Devuelve la lista de ID's de los tiles que contiene la capa.'''
	string = base64.decodestring(string)
	string = StringIO.StringIO(string)
	gzipper = gzip.GzipFile(fileobj=string)
	string = gzipper.read()
	l = []
	# http://sourceforge.net/apps/mediawiki/tiled/index.php?title=Examining_the_map_format
	for i in range(0, len(string), 4):
		gid = ord(string[i]) | ord(string[i+1])<<8 | ord(string[i+2])<<16 | ord(string[i+3])<<24
		l.append(gid)
	return l

def psplit(list, cols):
	'''Trocea una lista en listas con un cierto número de elementos.'''
	m = []
	for i in range(0, len(list), cols):
		m.append(list[i:i+cols])
	return m
