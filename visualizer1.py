""" This file contains the code for the visual representation of the tiles, grid etc"""

from queue import PriorityQueue
import pygame
import math

# To create a new window using pygame and set the name of the window
DEFAULT_WIDTH = 800
WINDOW = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_WIDTH))
pygame.display.set_caption('A* Pathfinding Visualizer')

# Define all the various color values to use on the tiles
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
TEAL = (0, 128, 128)
