import sys

import pygame

from three_r_robot import ThreeRRobot


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, robot_left_conf):
    screen.fill(settings.bg_color)
    robot_left_conf.blit_me()

    pygame.display.flip()