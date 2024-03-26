# Imports

import pygame
import sys
from pygame.locals import *


# Initialize, set up pygame

pygame.init() # Always need to be called before you do anything

# Set up window
windowSurface = pygame.display.set_mode((500, 400), 0, 32) # First argument is the dimensions of the display, second is the color "depth", and third is the "display" resolution (supposedly)
pygame.display.set_caption("Woomy")

# Set up colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Set up fonts
basicFont = pygame.font.SysFont(None, 48)

# Set up text
text = basicFont.render("Yippie", True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Set up background
windowSurface.fill(WHITE)

# Add shapes :)
pygame.draw.polygon(windowSurface, GREEN, ((146, 0),(291, 106),(236, 277),(56, 277),(0, 106)))

# Render/draw text on the screen
windowSurface.blit(text, textRect)


# Set up/draw the window onto the screen [Always needs to be last]
pygame.display.update()


# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()