from djitellopy import tello
from time import sleep

robot = tello.Tello()

robot.connect()
print("Drone Battery level: ",robot.get_battery())
robot.takeoff()
robot.send_rc_control(0,50,0,0) #move forward
sleep(2)
robot.send_rc_control(0,0,0,0)
robot.land()
