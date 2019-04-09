
import pygame

#class for controlling playback of Sound objects
class Mixer():

	def __init__(self):

		self.mixer = pygame.mixer

		self.mixer.pre_init(44100,-16,2,1024)
		self.mixer.init()

	def getMixer(self):

		return self.mixer
