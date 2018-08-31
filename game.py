import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf
from background import Background



def game_on():
	# Initalize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("DON'T KICK ME!")

	# Create a background for the game
	background = Background(screen)
	

	# Make a ship.
	ship = Ship(ai_settings, screen)

	# Make a group to store bullets and aliens in
	bullets = Group()
	aliens = Group()

	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Create an instance to store game statistics.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# Make the Play button.
	play_button = Button(ai_settings, screen, "Play")

	

	# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		gf.update_screen(ai_settings, stats, screen, sb, ship, bullets, aliens, play_button, background)


		if stats.game_active:
		# Redraw the screen during each pass through the loop.
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)


game_on()


	

