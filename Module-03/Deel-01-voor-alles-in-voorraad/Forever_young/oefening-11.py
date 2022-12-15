from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 3
for x in range(8):
    robotArm.moveRight()
for y in range(9):
    print(y)
    robotArm.grab()
    color = robotArm.scan() 
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()  
    else:
        robotArm.drop()
    if y < 8:
        robotArm.moveLeft()

robotArm.wait()