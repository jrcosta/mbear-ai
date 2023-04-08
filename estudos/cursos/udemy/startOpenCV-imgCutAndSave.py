import cv2

img = cv2.imread('./Curso1/OpenCVBasico/farol.jpg')

dim = cv2.selectROI("Selecione a Area de Recorte", img, False)
cv2.destroyWindow('Selecione a Area de Recorte')

posit1 = int(dim[0])
posit2 = int(dim[1])
posit3 = int(dim[2])
posit4 = int(dim[3])

imgCut = img[posit2:posit2+posit4, posit1:posit1+posit3]

path = './CutImg/'
nameImage = input('Digite o nome do arquivo')

cv2.imwrite(f'{path}{nameImage}.jpg', imgCut)

cv2.imshow('Teste Recorte', imgCut)
cv2.waitKey(0)