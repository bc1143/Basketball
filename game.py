import pygame
from pygame.locals import *

pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 1000, 750
screen = pygame.display.set_mode((width, height))
orange = (222, 133, 32)
black = (0, 0, 0)
grey = (135, 135, 135)
white = (255, 255, 255)
red = (255, 0, 0)

class Ball():
    def __init__(self):
        self.pos_x = 250
        self.pos_y = 500
        self.color = orange
        self.radius = 20
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        self.speed_y += 1
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

    def update(self):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.radius)


def drag():
    start_x, start_y = pygame.mouse.get_pos()
    drag_flag = True
    while drag_flag:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                end_x, end_y = pygame.mouse.get_pos()
                drag_flag = False
    return (start_x - end_x, start_y - end_y)

def collide_check(basketball, rim, backboard):
    top = (basketball.pos_x, (basketball.pos_y - basketball.radius))
    bottom = (basketball.pos_x, (basketball.pos_y + basketball.radius))
    left = ((basketball.pos_x - basketball.radius), basketball.pos_y)
    right = ((basketball.pos_x + basketball.radius), basketball.pos_y)
    for edge in [top, bottom, left, right]:
        if rim.collidepoint(edge) or backboard.collidepoint(edge):
            return True
    else:
        return False


def main():
    screen.fill(black)
    pole = pygame.Rect(900, 300, 20, 600)
    backboard = pygame.Rect(870, 200, 10, 200)
    rim = pygame.Rect(780, 350, 90, 10)
    pygame.draw.rect(screen, grey, pole)
    pygame.draw.rect(screen, white, backboard)
    pygame.draw.rect(screen, red, rim)
    background = screen.copy()
    basketball = Ball()
    move_flag = False
    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                delta_x, delta_y = drag()
                basketball.speed_x = delta_x // 5
                basketball.speed_y = delta_y // 5
                move_flag = True
        
        if move_flag:
            collide_flag = collide_check(basketball, rim, backboard)
            if collide_flag:
                basketball.speed_x = -(basketball.speed_x // 2)
                basketball.speed_x = -(basketball.speed_y // 2) 
            basketball.move()

        basketball.update()
        
        if (basketball.pos_x > 1020) or (basketball.pos_y > 800):
            basketball = Ball()
            move_flag = False

        pygame.display.flip()
        fpsClock.tick(fps)

main()