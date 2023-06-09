import cv2

img = cv2.imread('C:/Users/eneri.junior/mbear-ai/estudos/cursos/udemy/Curso1/OpenCVBasic/piramide.jpg')
img = cv2.resize(img,(500,400))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7, 7),0)
imgCanny = cv2.Canny(img, 50, 100)
imgDilat = cv2.dilate(imgCanny,(5,5),iterations=5)
imgErode = cv2.erode(imgCanny,(5,5),iterations=2)
imgOpening = cv2.morphologyEx(imgCanny, cv2.MORPH_OPEN,(5,5))
imgClose = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE,(5,5))



cv2.imshow('Img Orig', img)
cv2.imshow('Img Cinza', imgGray)
cv2.imshow('Img Blur', imgBlur)
cv2.imshow('Img Canny', imgCanny)
cv2.imshow('Img Dilate', imgDilat)
cv2.imshow('Img Erode', imgErode)
cv2.imshow('Img Opening', imgOpening)
cv2.imshow('Img Close', imgClose)
cv2.waitKey(0)