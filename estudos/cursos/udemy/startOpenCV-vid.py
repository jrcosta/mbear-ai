import cv2

video = cv2.VideoCapture('./Curso1/OpenCVBasico/runners.mp4')

while True:
    check, img = video.read()
    print(img.shape)
    imgRedim = cv2.resize(img,(640, 420))
    cv2.imshow('Teste video', imgRedim)
    cv2.waitKey(0)
