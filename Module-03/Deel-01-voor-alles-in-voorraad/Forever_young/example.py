from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')

color = robotArm.scan() 
robotArm.grab()
if color == "white":
    robotArm.moveRight()
    robotArm.drop()
else:
    robotArm.drop
    robotArm.moveRight()
    robotArm.grab()
    robotArm.scan()
        
robotArm.wait()