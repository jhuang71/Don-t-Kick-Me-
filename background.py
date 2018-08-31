import pygame
from pygame.sprite import Sprite
import settings
class Background(Sprite):
	
	def __init__(self, screen):
		super(Background, self).__init__()
		self.screen = screen
		self.image = pygame.image.load('images/snowdownv1.png')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

	# Create the background image
	def blitme(self):
		self.screen.blit(self.image, self.rect)



