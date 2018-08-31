import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position"""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings


		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/teemo1.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)

		# flag movement statement
		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.move_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		# Update rect object from self.center.
		self.rect.centerx = self.center

	def center_ship(self):
		"""Center the ship"""
		self.center = self.screen_rect.centerx



		
