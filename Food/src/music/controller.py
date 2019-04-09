## @file   controller.py
#  @title  Music player controller
#  @author Alex Lo
#  @date   April 08, 2019


import pygame
import game

class MixerController():

	def __init__(self):

		self.mixer = pygame.mixer

		self.mixer.pre_init(44100,16,2,4096)
		self.mixer.init()


	def loadMusic(self, songName):

		self.mixer.music.load(songName)
		self.mixer.music.set_volume(1)
		print("loaded music")

	def playMusic(self):

		self.mixer.music.play(-1)

	def stopMusic(self):

		self.mixer.music.stop()

	def playSoundEffect(self, soundName):

		self.mixer.Sound(soundName).play()
		#print(self.mixer.Sound(soundName).get_volume())



