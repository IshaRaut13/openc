import cv2
import random

img = cv2.imread("assets/logo.jpg", -1)

for i in range(100):  # 100 rows
    for j in range(img.shape[1]):  # changing the one column color
        img[i][j] = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ]  # generates a random number btw the (low, high) value

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
