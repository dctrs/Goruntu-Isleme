import  cv2
import numpy as np
import matplotlib.pyplot as plt
flower = cv2.imread("flower.jpg")

s=flower.shape

flowerG = cv2.cvtColor(flower,cv2.COLOR_BGR2GRAY)


H=np.zeros(shape=(256,1))

for i in range(s[0]):
    for j in range(s[1]):
        k=flowerG[i,j]
        H[k,0]=H[k,0]+1
print(H)
plt.plot(H)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
