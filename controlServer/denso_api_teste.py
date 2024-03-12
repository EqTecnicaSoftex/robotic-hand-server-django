import rria_api_denso

ria = rria_api_denso.DensoRobotAPI('', '', 'Server=IP')  # workspace, control, options

ria.connect()

if ria.is_connected():
    print("Connected")
    ria.motor_on()

    if ria.motor_enabled():
        ria.set_arm_speed(30, 30, 30)  # speed, accel, decel
        ria.move_joints(rria_api_denso.RobotJointCommand(0, 0, 0, 0, 0, 0))
        ria.motor_off()
    else:
        print("Motor off")
else:
    print("Not connected")
