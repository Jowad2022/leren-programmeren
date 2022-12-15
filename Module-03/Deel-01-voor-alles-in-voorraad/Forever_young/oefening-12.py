from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 2
for s in range(9,0,-1):
    robotArm.grab()
    color = robotArm.scan() 
    if color == "red":
        for x in range(s):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(x):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()