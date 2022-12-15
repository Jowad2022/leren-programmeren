from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for x in range(7):
    robotArm.grab()
    for z in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for f in range(8):
        robotArm.moveLeft()
robotArm.wait()