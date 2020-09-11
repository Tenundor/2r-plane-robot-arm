import pygame

from settings import Settings
import program_functions as pf
from three_r_robot import ThreeRRobot


def run_program():
    pygame.init()
    clock = pygame.time.Clock()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("3R inverse kinematic")

    robot_left_conf = ThreeRRobot(screen, tau_list=[2, -1, 2], length_list=[2, 1, 0.5])

    while True:
        pf.check_events()
        pf.update_screen(settings, screen, robot_left_conf)

        clock.tick(5)


run_program()
