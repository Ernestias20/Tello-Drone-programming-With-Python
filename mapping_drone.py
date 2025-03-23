from djitellopy import tello
import key_press_module as kp
import numpy as np
import cv2
import math
from time import sleep

#### PARAMETERS ###
fSpeed = 117/10  #forward speed in cm/s, 15cm/s
aSpeed = 360/10 #Angular speed in Degrees/s
interval = 0.25
dInterval = fSpeed*interval
aInterval = aSpeed*interval
###############################
x,y = 500,500

a = 0
kp.init()

robot = tello.Tello()
robot.connect()
print("Battery Level: ",robot.get_battery())
points = []
def getKeyBoardInput():
  lr,fb,ud,yv = 0,0,0,0
  speed = 15
  aspeed = 50
  sleep(0.25)
  global yaw,x,y,a
  d = 0
  yaw = 0
  if kp.getKey("LEFT"):
      lr = -speed
      d = dInterval
      a =  -180
  elif kp.getKey("RIGHT"):
      lr = speed
      d = -dInterval
      a = 180
  if kp.getKey("UP"):
    fb = speed
    d = dInterval
    a = 270
  elif kp.getKey("DOWN"):
    fb = -speed
    d = -dInterval
    a = -90
  if kp.getKey("w"):
    ud = speed
  elif kp.getKey("s"):
    ud = -speed

  if kp.getKey("a"):
    yv = -aspeed
    yaw -= aInterval
  elif kp.getKey("d"):
    yv = aspeed
    yaw += aInterval
  if kp.getKey("q"):
     robot.land()
  if kp.getKey("e"):
     robot.takeoff()

  a += yaw
  x += int(d*math.cos(math.radians(a)))
  y += int(d*math.sin(math.radians(a)))
  return [lr,fb,ud,yv,x,y]

def drawPoints(img,points):
    for point in points:
        cv2.circle(img,point,5,(0,0,255),cv2.FILLED)
    cv2.putText(img,f'({(points[-1][0] - 500)/100},{(points[-1][1] - 500)/100})m',
                (points[-1][0]+10,points[-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,
                (255,0,255),1)
while True:
   vals = getKeyBoardInput()
   robot.send_rc_control(vals[0],vals[1],vals[2],vals[3])

   img = np.zeros((1000,1000,3))
   points.append((vals[4],vals[5]))
   drawPoints(img,points)
   cv2.imshow("Output",img)
   cv2.waitKey(1)