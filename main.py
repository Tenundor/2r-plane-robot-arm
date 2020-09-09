import pygame

from settings import Settings
import program_functions as pf


def run_program():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("3R inverse kinematic")

    while True:
        pf.check_events()
        pf.update_screen(settings,screen)


run_program()