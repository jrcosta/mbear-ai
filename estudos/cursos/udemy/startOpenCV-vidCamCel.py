import cv2

video = cv2.VideoCapture()
ip = "https://192.168.0.2:8080/video" #Ip gerado no aplicativo IP Webcam
video.open(ip)

while True:
    check, img = video.read()
    imgRedim = cv2.resize(img,(640, 420))
    cv2.imshow('Teste video', imgRedim)
    cv2.waitKey(1)
