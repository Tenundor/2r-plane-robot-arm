import pygame
import math as m


class ThreeRRobot:

    def __init__(self, screen, scale_px_m=None, joint1_coord=None, tau_list=None, length_list=None, robot_color=None):
        if scale_px_m is None:
            scale_px_m = 100
        if length_list is None:
            length_list = [1, 1, 1]

        self.max_length_px = int(sum(length_list) * scale_px_m + 0.5)

        if joint1_coord is None:
            joint1_coord = [self.max_length_px + 50, self.max_length_px + 50]
        if tau_list is None:
            tau_list = [0, 0, 0]

        if robot_color is None:
            robot_color = (244, 240, 235)

        self.screen = screen
        self.scale_px_m = scale_px_m
        self.tau_list = tau_list
        self.length_list = length_list
        self.robot_color = robot_color

        self.joints = [joint1_coord]

        for count in range(len(self.tau_list)):
            tau_sum = sum(self.tau_list[:count + 1])
            current_joint_x = self.joints[-1][0] + int(
                self.length_list[count] * m.cos(tau_sum) * self.scale_px_m + 0.5)
            current_joint_y = self.joints[-1][1] - int(
                self.length_list[count] * m.sin(tau_sum) * self.scale_px_m + 0.5)
            current_joint = [current_joint_x, current_joint_y]
            self.joints.append(current_joint)

    def blit_me(self):
        pygame.draw.rect(self.screen, self.robot_color, (self.joints[0][0] - 40, self.joints[0][0], 80, 20))
        pygame.draw.lines(self.screen, self.robot_color, False, self.joints, 10)

        for count in range(len(self.tau_list)):
            pygame.draw.circle(self.screen, self.robot_color, self.joints[count], 15)
