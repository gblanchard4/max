#! /usr/bin/env python

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
STAR helper class
'''

class Star:
	def __init__(self, binary, extension, genome, clip5pNbases, outFilterMultimapNmax):
		self.binary = binary
		self.extension = extension
		self.genome = genome
		self.clip5pNbases = clip5pNbases
		self.outFilterMultimapNmax

	def command_builder(self):
		command = 


