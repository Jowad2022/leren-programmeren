from RobotArm import RobotArm
robotArm = RobotArm('exercise 10') 
robotArm.speed = 3
for y in range(9,0,-2):
    robotArm.grab()
    for k in range(y):
        robotArm.moveRight()
    robotArm.drop()
    for z in range(k,0,-1):
        robotArm.moveLeft()
robotArm.wait()