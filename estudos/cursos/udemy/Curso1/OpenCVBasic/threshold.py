import cv2

img1 = cv2.imread('./Curso1/OpenCVBasico/img01.jpg')
img2 = cv2.imread('./Curso1/OpenCVBasico/img02.jpg')
img1r = cv2.resize(img1, (700,800))
img2r = cv2.resize(img2, (700,800))
img1Gray = cv2.cvtColor(img1r,cv2.COLOR_BGR2GRAY)
img2Gray = cv2.cvtColor(img2r,cv2.COLOR_BGR2GRAY)

_,th1 = cv2.threshold(img1Gray, 127, 255, cv2.THRESH_BINARY_INV)
th2 = cv2.adaptiveThreshold(img2Gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 16)
th3 = cv2.adaptiveThreshold(img2Gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 16)

cv2.imshow('Original1', img1r)
cv2.imshow('Original2', img2r)
cv2.imshow('Th1', th1)
cv2.imshow('Th2', th2)
cv2.imshow('Th3', th3)
cv2.waitKey(0)