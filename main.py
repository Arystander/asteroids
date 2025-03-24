import pygame
from player import Player
from constants import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH /2
	y = SCREEN_HEIGHT / 2
	Player.containers = (updatable, drawable)
	player = Player(x,y)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		updatable.update(dt)
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		dt = (clock.tick(60)) / 1000



if __name__ == "__main__":
	main()
