import cv2
import mediapipe as mp
import math
import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
mp_drawing = mp.solutions.drawing_utils

start = 0
status = ""

while True:
    check, img = video.read()
    img = cv2.resize(img, (1000, 720))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    h, w, _ = img.shape
    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            # mp_drawing.draw_landmarks(img, face, mpFaceMesh.FACEMESH_FACE_OVAL)
            pointEyeR1x, pointEyeR1y = int(
                (face.landmark[159].x)*w), int((face.landmark[159].y)*h)
            pointEyeR2x, pointEyeR2y = int(
                (face.landmark[145].x)*w), int((face.landmark[145].y)*h)

            pointEyeL1x, pointEyeL1y = int(
                (face.landmark[386].x)*w), int((face.landmark[386].y)*h)
            pointEyeL2x, pointEyeL2y = int(
                (face.landmark[374].x)*w), int((face.landmark[374].y)*h)

            cv2.circle(img, (pointEyeR1x, pointEyeR1y), 1, (255, 255, 0), 2)
            cv2.circle(img, (pointEyeR2x, pointEyeR2y), 1, (255, 255, 0), 2)
            cv2.circle(img, (pointEyeL1x, pointEyeL1y), 1, (255, 255, 0), 2)
            cv2.circle(img, (pointEyeL2x, pointEyeL2y), 1, (255, 255, 0), 2)

            distPointsR = math.hypot(
                pointEyeR1x-pointEyeR2x, pointEyeR1y-pointEyeR2y)
            distPointsL = math.hypot(
                pointEyeL1x-pointEyeL2x, pointEyeL1y-pointEyeL2y)

            if distPointsR <= 10 and distPointsL <= 10:
                cv2.rectangle(img, (100, 30), (390, 80), (0, 0, 255), -1)
                cv2.putText(img, "CLOSED EYES", (105, 65),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255,), 3)
                situation = "C"
                if situation != status:
                    start = time.time()
            else:
                cv2.rectangle(img, (100, 30), (370, 80), (0, 255, 0), -1)
                cv2.putText(img, "OPEN EYES", (105, 65),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255,), 3)
                situation = "O"
                start = time.time()
                timeEye = int(time.time()-start)

            if situation == "C":
                timeEye = int(time.time()-start)

            status = situation

            if timeEye >= 2:
                cv2.rectangle(img, (300,150), (850,220), (0,0,255), -1)
                cv2.putText(img, f'SLEEPING {timeEye} SEG', (310,200), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255,255,255), 5)
                
    cv2.imshow('Imagem', img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
