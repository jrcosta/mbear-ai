import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pointsN = []

    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x*w), int(cord.y*h)
                #cv2.putText(img, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                pointsN.append((cx, cy))
        fingers = [8, 12, 16, 20]
        count = 0

        if pointsN:
            if pointsN[4][0] < pointsN[2][0]:
                count += 1
            for x in fingers:
                if pointsN[x][1]< pointsN[x-2][1]:
                    count += 1
        cv2.rectangle(img, (80,10), (200,100), (0,255,0),-1)
        cv2.putText(img, str(count), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0,0,255), 5)
    cv2.imshow('Imagem', img)
    cv2.waitKey(1)