import cv2

camera = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier('C:/Users/eneri.junior/mbear-ai/estudos/cursos/udemy/Curso1/OpenCVBasic/Haarcascade/cascades/haarcascade_eye.xml')

while True:
    check, img = camera.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = classifier.detectMultiScale(imgGray, minSize=(30,30), scaleFactor=1.5)

    for x, y, w, h in objects:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('Imagem Cam', img)
    cv2.waitKey(1)