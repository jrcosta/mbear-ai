import cv2

img = cv2.imread('./Curso1/OpenCVBasico/farol.jpg')

imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img.shape, "Imagem RGB")
print(imgCinza.shape, "Imagem Cinza")

cv2.imshow('Teste Imagem', img)
cv2.imshow('Teste Imagem Cinza', imgCinza)

cv2.waitKey(0)