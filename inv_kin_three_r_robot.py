import math as m
import functools as ft


def inv_kin_3r_robot(end_ef_coord, end_ef_angle_degree, link_length_list):
    end_ef_angle = m.radians(end_ef_angle_degree)
    joint_3_x = end_ef_coord[0] - link_length_list[2] * m.cos(end_ef_angle)
    joint_3_y = end_ef_coord[1] - link_length_list[2] * m.sin(end_ef_angle)
    links_1_2_diff = link_length_list[0] - link_length_list[1]

    if (joint_3_x ** 2 + joint_3_y ** 2) < links_1_2_diff ** 2 or (joint_3_x ** 2 + joint_3_y ** 2) > sum(link_length_list) ** 2:
        robot_config = {'robot_config': {'left_robot_tau_list': [0, 0, 0],
                                         'right_robot_tau_list': [0, 0, 0]},
                        'work_space_out': True}
        return robot_config

    cos_alpha = (joint_3_x ** 2 + joint_3_y ** 2 + link_length_list[0] ** 2 - link_length_list[1] ** 2) / (
            2 * m.sqrt(joint_3_x ** 2 + joint_3_y ** 2) * link_length_list[0]
    )

    alpha = m.acos(cos_alpha)
    cos_beta = (link_length_list[0] ** 2 + link_length_list[1] ** 2 - joint_3_x ** 2 - joint_3_y ** 2) / (
        2 * ft.reduce(lambda x, y: x * y, link_length_list)
    )
    beta = m.acos(cos_beta)
    gamma = m.atan2(joint_3_y, joint_3_x)

    i = -1
    tau_1 = []
    tau_2 = []
    tau_3 = []
    all_tau_list = [tau_1, tau_2, tau_3]
    while i < 2:
        tau_1.append(gamma + i * alpha)
        tau_2.append(i * (beta - m.pi))
        tau_3.append(end_ef_angle - tau_2[-1] - tau_1[-1])
        i += 2

    left_robot_tau_list = list(map(lambda x: x[0], all_tau_list))
    right_robot_tau_list = list(map(lambda x: x[1], all_tau_list))

    robot_config = {'robot_config': {'left_robot_tau_list': left_robot_tau_list,
                                     'right_robot_tau_list': right_robot_tau_list},
                    'work_space_out': False}

    return robot_config
