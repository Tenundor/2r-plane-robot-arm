from inv_kin_three_r_robot import inv_kin_3r_robot
print('Hello')
test_robot = inv_kin_3r_robot([1, 1], 0, [2, 2, 1])
print(test_robot['robot_config']['left_robot_tau_list'])
