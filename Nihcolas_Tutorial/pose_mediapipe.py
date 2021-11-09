import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

if __name__ == '__main__':
	
	cap = cv2.VideoCapture(0)
	
	grabbed, frame = cap.read()
	
	while grabbed:
		cv2.imshow("Mediapipe Feed", frame)
		if cv2.waitkey(10) & 0xFF == ord('q'):
			break
		grabbed, frame = cap.read()

	cap.release()
	cv2.destroyAllWindows()

