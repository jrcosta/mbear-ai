import cv2
import pickle
import numpy as np

spaces = []
with open('./estudos/cursos/udemy/Curso1/OpenCVBasic/spaces.pkl', 'rb') as file:
    spaces = pickle.load(file)

video = cv2.VideoCapture('./estudos/cursos/udemy/Curso1/OpenCVBasic/video.mp4')

while True:
    check, img = video.read()
    if check:
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgTH = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
        imgMededian = cv2.medianBlur(imgTH, 5)
        kernel = np.ones((3,3), np.int8)
        imgDil = cv2.dilate(imgMededian, kernel)
    else:
        break
    
    openSpaces = 0
    for x, y, w, h in spaces:
        space = imgDil[y:y+h,x:x+w]
        count = cv2.countNonZero(space)
        if count < 900:
            openSpaces += 1
        cv2.rectangle(img, (90,0), (415,60), (0,255,0), -1)
        cv2.putText(img, f'OPEN: {openSpaces}/69', (95, 45), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255,255,255), 5)
        

    cv2.imshow('Video',img)
    cv2.waitKey(1)

# Este trecho de código é um exemplo de como processar um vídeo com o OpenCV para detectar espaços de estacionamento vazios.
#
# O programa começa lendo um arquivo de vídeo usando a função cv2.VideoCapture(), que retorna um objeto de captura de vídeo. Em seguida, ele entra em um loop infinito, lendo cada quadro do vídeo um de cada vez usando a função video.read(). O loop termina quando o vídeo chega ao fim ou o usuário pressiona a tecla 'q'.
#
# Para cada quadro do vídeo, o programa faz o seguinte processamento:
#
# Converte o quadro para escala de cinza usando a função cv2.cvtColor().
# Aplica uma limiarização adaptativa usando a função cv2.adaptiveThreshold(), que calcula um valor de limiar local para cada pixel com base na intensidade dos pixels vizinhos.
# Aplica um filtro de mediana para suavizar a imagem e remover o ruído.
# Cria um kernel 3x3 usando a função np.ones() e np.int8() e usa a função cv2.dilate() para dilatar as áreas brancas da imagem, a fim de preencher pequenas lacunas e melhorar a precisão da detecção de espaços vazios.
# Em seguida, o programa percorre a lista de coordenadas de espaços de estacionamento (previamente salvas em um arquivo pickle e carregadas usando a função pickle.load()), e para cada espaço, recorta a região correspondente da imagem dilatada. A função cv2.countNonZero() é usada para contar o número de pixels brancos na região. Se o número de pixels brancos é menor que um valor de limiar (definido como 900 no código), o espaço é considerado vazio e o contador openSpaces é incrementado.
#
# Finalmente, o programa exibe o quadro processado com retângulos sobre cada espaço de estacionamento e um texto mostrando o número de espaços vazios detectados.
