import cv2

video = cv2.VideoCapture(0)


sample = 1
while True:
    check, img = video.read()
    imgCinca = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        imgRedim = cv2.resize(imgCinca, (220,220))
        cv2.imwrite(f'/Curso1/OpenCVBasic/Haarcascade/cascadeTraining/photos/positive/im{sample}.jpg', imgRedim)
        sample += 1

        
    cv2.imshow("Capture", img)
    cv2.waitKey(1)