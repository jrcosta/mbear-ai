import cv2

img = cv2.imread('./Curso1/OpenCVBasic/objetos.jpg')
img = cv2.resize(img, (500,400))

imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(imgCinza, 30, 200)
imgClose = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, (7,7))

contours, hierarchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

numObj = 1
for cnt in contours:
    #cv2.drawContours(img, cnt, -1, (255,0,0), 2)
    x, y, w, h = cv2.boundingRect(cnt)
    object = img[y:y+h,x:x+w]
    cv2.imwrite(f'./Curso1/OpenCVBasic/Object/Object{numObj}.jpg', object)
    cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,0), 2)
    numObj += 1

cv2.imshow('Imagem', img)
cv2.waitKey(0)