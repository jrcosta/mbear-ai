import cv2

img = cv2.imread('C:/Users/eneri.junior/mbear-ai/estudos/cursos/udemy/Curso1/OpenCVBasico/piramide.jpg')
img = cv2.resize(img,(500,400))

video = cv2.VideoCapture('C:/Users/eneri.junior/mbear-ai/estudos/cursos/udemy/Curso1/OpenCVBasico/runners.mp4')

while True:
    check, img = video.read()
    imgRedim = cv2.resize(img,(1024, 760))

    cv2.rectangle(imgRedim, (50,50),(200,200),(1,20,150),5)

    cv2.circle(imgRedim, (300,300), 50, (255,20,200), 5)

    cv2.line(imgRedim, (250,250), (400,200),(0,255,200), 2)

    texto = 'Ola Mundo!'

    cv2.putText(imgRedim, texto, (50,100),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,1), 2)

    cv2.imshow('Teste video', imgRedim)


    cv2.waitKey(0)