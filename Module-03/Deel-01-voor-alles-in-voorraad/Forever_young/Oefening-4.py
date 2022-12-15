from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

for x in range(1,6):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
    
robotArm.moveRight()
robotArm.moveRight()

for x in range(1,6):
    robotArm.grab()
    robotArm.moveLeft()   
    robotArm.drop()
    robotArm.moveRight()
    
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
