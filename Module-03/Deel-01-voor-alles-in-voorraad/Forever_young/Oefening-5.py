from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

for x in range(7):
    robotArm.moveRight()
for i in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
    
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
