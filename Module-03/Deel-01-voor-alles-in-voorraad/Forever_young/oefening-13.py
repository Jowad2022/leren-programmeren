from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.speed = 3
robotArm.randomLevel(1,7)

i = 1
while robotArm.grab():
    for y in range(i):
        robotArm.moveRight()
    robotArm.drop()
    for y in range(i):
        robotArm.moveLeft()
    i += 1     
robotArm.wait()