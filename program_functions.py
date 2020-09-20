import sys

import pygame

import math as m


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def animate_joints(tau_list, velocity_list, max_angle=4 * m.pi):
    if max(tau_list, key=abs) < max_angle:
        new_tau_list = [x + y for x, y in zip(tau_list, velocity_list)]
        return {'tau_list': new_tau_list, 'max_angle_flag': False}
    else:
        return {'tau_list': tau_list, 'max_angle_flag': True}


def update_screen(settings, screen, robot_left_conf):
    screen.fill(settings.bg_color)
    robot_left_conf.update()
    robot_left_conf.blit_me()

    pygame.display.flip()
