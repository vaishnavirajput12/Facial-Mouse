import cv2
#mediapipe is used to detect fingers
import mediapipe as mp
import pyautogui                                     #for controlling mouse
def mousedetector():
  hand_detector = mp.solutions.hands.Hands()  #by using hands solution we called Hands method
  drawing_utils = mp.solutions.drawing_utils  #to draw landmarks
#used to record video and video will be stored inside var cap
#video capture method is used to capture the video on 0 sec..matlab turant video capture karo
  cap = cv2.VideoCapture(0)
  screen_width , screen_height = pyautogui.size()
  index_y =0
#video continue record krte jaane keliye:
  while True:
   _, frame = cap.read()
   frame =cv2.flip(frame, 1)
   frame_height , frame_width ,_ = frame.shape    #using to multiply width of frame to multiply with x
   rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   output  = hand_detector.process(rgb)
   hands = output.multi_hand_landmarks
   if hands:
      for hand in hands:
        drawing_utils.draw_landmarks(frame ,hand) #frame is used so that hume maalum re ki hamare landmark frame ke andar hai
        landmarks = hand.landmark
        for id, landmark in enumerate( landmarks):
               x= int(landmark.x*frame_width) #as x is horizontal its multiplied by width
               y =int(landmark.y*frame_height )  #as y is vertical its multiplied by height


               if id==8:   #for index finger top numbr is 8
                   cv2.circle(img=frame , center=(x,y) , radius=10, color=(0,255,255))
                   index_x=screen_width/frame_width*x
                   index_y=screen_height/frame_height*y
                   pyautogui.moveTo(index_x, index_y)
               if id == 4:  # for thumb top numbr is 4 (clicking)
                       cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                       thumb_x = screen_width / frame_width * x
                       thumb_y = screen_height / frame_height * y
                       print(abs( index_y - thumb_y))
                       if abs( index_y - thumb_y) < 45:
                         pyautogui.click()
                         pyautogui.sleep(1)
  #to show the img:
   cv2.imshow('VIRTUAL MOUSE',frame)
   cv2.waitKey(1)


