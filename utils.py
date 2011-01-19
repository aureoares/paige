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
