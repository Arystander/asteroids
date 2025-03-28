import pygame
import sys
from player import Player
from constants import *
from asteroidfield import *
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH /2
	y = SCREEN_HEIGHT / 2
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	asteroidfield = AsteroidField()
	player = Player(x,y)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0,0,0))

		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					shot.kill()
					asteroid.split()


		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		dt = (clock.tick(60)) / 1000



if __name__ == "__main__":
	main()
