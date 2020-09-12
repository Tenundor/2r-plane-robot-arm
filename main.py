import pygame
import math as m

from settings import Settings
import program_functions as pf
from three_r_robot import ThreeRRobot
from inv_kin_three_r_robot import inv_kin_3r_robot


def run_program():
    pygame.init()
    clock = pygame.time.Clock()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("3R inverse kinematic")

    test_robot_length_list = [3, 2, 1]
    test_robot_end_eff_coord = [4, 2]
    test_robot_end_eff_angle = 0
    test_robot_tau_list = inv_kin_3r_robot(test_robot_end_eff_coord, test_robot_end_eff_angle, test_robot_length_list)
    robot_left_conf = ThreeRRobot(screen, tau_list=test_robot_tau_list['robot_config']['right_robot_tau_list'],
                                  length_list=test_robot_length_list, scale_px_m=50)

    while True:
        pf.check_events()
        pf.update_screen(settings, screen, robot_left_conf)

        clock.tick(30)


run_program()
