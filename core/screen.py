import pygame
from core.textures.font import Font
from pygame import Color
from pygame import display
import sys
import os


screen = None
dims = None
wh = None


def initiate(dim, texdim): #dim and texdim both tuples of ints
    global screen
    global dims
    global wh
    dims = dim
    wh = texdim
    screen = display.set_mode((dim[0] * texdim[0], dim[1] * texdim[1]))


def calcpos(raw):
    return raw[0] * dims[0], raw[1] * dims[1]


# initiate((64 + 32, 32 + 4), (12, 18))
# f = Font('../fonts/AS.png')
# f.drawbasic(screen, 'Hello there sirs', (0, 0))
# display.update()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()