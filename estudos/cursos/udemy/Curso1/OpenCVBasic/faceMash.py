import cv2
import mediapipe as mp

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
mp_drawing = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    img = cv2.resize(img, (1000,720))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    h, w, _ = img.shape
    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            #mp_drawing.draw_landmarks(img, face, mpFaceMesh.FACEMESH_FACE_OVAL)
            pointEyeR1x, pointEyeR1y = int((face.landmark[159].x)*w), int((face.landmark[159].y)*h)
            pointEyeR2x, pointEyeR2y = int((face.landmark[145].x)*w), int((face.landmark[145].y)*h)

            pointEyeL1x, pointEyeL1y = int((face.landmark[386].x)*w), int((face.landmark[386].y)*h)
            pointEyeL2x, pointEyeL2y = int((face.landmark[374].x)*w), int((face.landmark[374].y)*h)

            cv2.circle(img, (pointEyeR1x,pointEyeR1y), 1, (255, 255, 0), 2 )
            cv2.circle(img, (pointEyeR2x,pointEyeR2y), 1, (255, 255, 0), 2)
            cv2.circle(img, (pointEyeL1x,pointEyeL1y), 1, (255, 255, 0), 2)
            cv2.circle(img, (pointEyeL2x,pointEyeL2y), 1, (255, 255, 0), 2)

    cv2.imshow('Imagem', img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
