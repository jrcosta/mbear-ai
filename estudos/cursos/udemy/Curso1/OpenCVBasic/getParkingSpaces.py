import cv2
import pickle

img = cv2.imread('./estudos/cursos/udemy/Curso1/OpenCVBasic/estacionamento.png')

spaces = []

for x in range(69):
    space = cv2.selectROI('Spaces', img, False)
    cv2.destroyWindow('Spaces')
    spaces.append((space))

    for x, y, w, h in spaces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0), 2)

with open('spaces.pkl','wb') as file:
    pickle.dump(spaces,file)