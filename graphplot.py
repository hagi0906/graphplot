import cv2
import matplotlib.pyplot as plt

i = 0
j = 0
x = []
y = []
plt.ion()
 
cap = cv2.VideoCapture(0)
 
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
 
    ret,frame = cap.read()

    print(frame.mean())

    i = i + 1
    j = frame.mean()
    x.append(i)
    y.append(j)
    plt.plot(x,y)

    plt.draw()

    plt.pause(1)

    if i == 30:
        break
 
cap.release()
cv2.destroyAllWindows()