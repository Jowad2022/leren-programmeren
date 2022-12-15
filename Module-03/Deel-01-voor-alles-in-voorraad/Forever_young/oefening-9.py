from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for x in range(1,5):    
    for r in range(x):  
        robotArm.grab()
        for y in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()