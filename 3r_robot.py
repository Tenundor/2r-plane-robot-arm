import pygame
import math as m

class ThreeRRobot:

    def __init__(self, screen, scale_px_m=None, joint1_x=None, joint1_y=None, tau_list=None, length_list=None):
        if scale_px_m is None:
            scale_px_m = 100
        if length_list is None:
            length_list = [1, 1, 1]
        if joint1_x is None:
            joint1_x = self.max_length_px + 50
        if joint1_y is None:
            joint1_y = self.max_length_px + 50
        if tau_list is None:
            tau_list = [0, 0, 0]


        self.screen = screen
        self.max_length_px = int(sum(length_list) * scale_px_m + 0.5)
        self.surface = pygame.Surface((self.max_length_px * 2, self.max_length_px * 2))
        self.scale_px_m = scale_px_m
        self.joint1_x = joint1_x
        self.joint1_y = joint1_y
        self.tau_list = tau_list
        self.length_list = length_list

        self.joint2_x = self.joint1_x + int(length_list[0] * m.cos(tau_list[0]) * scale_px_m + 0.5)
        self.joint2_y = self.joint1_y + int(length_list[0] * m.sin(tau_list[0]) * scale_px_m + 0.5)
        self.joint3_x = self.joint2_x + int(length_list[1] * m.cos(sum.tau_list[:2]) * scale_px_m + 0.5)
        self.joint3_y = self.joint2_y + int(length_list[1] * m.sin(sum.tau_list[:2]) * scale_px_m + 0.5)
        self.end_effector_x = self.joint3_x + int(length_list[2] * m.cos(sum.tau_list[:3]) * scale_px_m + 0.5)
        self.end_effector_y = self.joint3_y + int(length_list[2] * m.sin(sum.tau_list[:3]) * scale_px_m + 0.5)



    def update(self):
