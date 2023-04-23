import cv2
import mediapipe as mp
import math

video = cv2.VideoCapture('./estudos/cursos/udemy/Curso1/OpenCVBasic/ANEXO+polichinelos.mp4')
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils
count = 0
check = True

while True:
    check, img = video.read()

    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRGB)
    points = results.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    h, w, _ = img.shape


    if points:
        footRy = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y*h)
        footRx = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x*w)
        footLy = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y*h)
        footLx = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x*w)
        handRy = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y*h)
        handRx = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x*w)
        handLy = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y*h)
        handLx = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x*w)

        distHand = math.hypot(handRx-handLx, handRy-handLy)
        distFoot = math.hypot(footRx-footLx, footRy-footLy)

        if check == True and distHand <= 150 and distFoot >= 150:
            count += 1
            check = False
        if distHand > 150 and distFoot < 150:
            check = True

        text = f'Qtd: {count}'
        cv2.putText(img, text, (40,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))

    cv2.imshow('Video', img)
    cv2.waitKey(40)