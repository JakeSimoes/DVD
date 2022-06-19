import random
import time

import colorsys
import pygame
import win32api
import win32con
import win32gui

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    global loop
    w = surface.get_width()
    h = surface.get_height()
    r, g, b, _ = color

    if (imageColor[0] != 0) & (loop == False):
        imageColor[0] -= 1
        imageColor[1] += 1
    elif imageColor[1] != 0:
        imageColor[1] -= 1
        imageColor[2] += 1
        loop = True
    elif imageColor[2] != 0:
        imageColor[2] -= 1
        imageColor[0] += 1
        if imageColor[2] == 0:
            loop = False


    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, pygame.NOFRAME) # For borderless, use pygame.NOFRAME

grey = (1,1,1)  # Transparency color

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*grey), 0, win32con.LWA_COLORKEY)

image = pygame.image.load(r'./dvd.png').convert_alpha()
x, y = image.get_size()
image = pygame.transform.scale(image, (int(x/4), int(y/4))).convert_alpha()

imageColor = [255,0,0]
changeX = 1
changeY = 1
posX = 0
posY = 0
loop = False
bound_x, bound_y = screen.get_width(), screen.get_height()
print(bound_x, bound_y)
running = True
while running:
    if pygame.display.get_active() == False:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False

    screen.fill(grey)  # Transparent background
    dvd_blit = screen.blit(image, (posX, posY))
    # TODO: Think of an algorithm for making satisfying movement.
    randX, randY = random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)
    if (posX + 286 > bound_x  or posX < 0):
        print("X")
        posX += (1 if changeX < 0 else -1) * 3
        changeX = (1 if changeX < 0 else -1)*random.uniform(1.0,3.0)
        changeY = (1 if random.random() < 0.5 else -1)*random.uniform(1.0,3.0)
    elif ((posY + 139) > bound_y or posY < 0):
        print("Y")
        posY += (1 if changeY < 0 else -1) * 3
        changeY = (1 if changeY < 0 else -1) * random.randint(1, 3)
        changeX = (1 if random.random() < 0.5 else -1) * random.randint(1, 3)
    fill(image, pygame.Color(imageColor))
    posX += changeX
    posY += changeY
    time.sleep(.005)

    pygame.display.update()