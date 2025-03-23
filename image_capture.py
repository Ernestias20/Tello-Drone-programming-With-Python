from djitellopy import tello
import cv2

robot = tello.Tello()
robot.connect()
print("Drone Battery Level: ",robot.get_battery())

robot.streamon()
while True:
    img = robot.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("Image",img)
    cv2.waitKey(1)