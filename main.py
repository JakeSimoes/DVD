import random

import pygame
import win32api
import win32con
import win32gui

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


posX = 0
posY = 0
randX = 0
xVector = 0.7
yVector = 0.7
xVector_temp = 0.7
yVector_temp = 0.7
bound_x, bound_y = screen.get_width(), screen.get_height()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False

    screen.fill(grey)  # Transparent background
    dvd_blit = screen.blit(image, (posX, posY))
    # TODO: Think of an algorithm for making satisfying movement.
    if (posX > bound_x - dvd_blit.width or posX < 0) or (posY > bound_y - dvd_blit.height or posY < 0):
        randX, randY = random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)
        xVector = xVector_temp
        yVector = yVector_temp
        xVector_temp = xVector
        yVector_temp = yVector
        xVector = -xVector_temp + randX
        yVector = -yVector_temp + randY

    posX += xVector
    posY += yVector

    pygame.display.update()