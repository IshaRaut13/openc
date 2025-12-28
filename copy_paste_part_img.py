import cv2

img = cv2.imread("assets/logo.jpg", -1)

# copy and paste
# tag = img[row:row, col:col]
tag = img[500:700, 600:900]
img[100:300, 500:800] = tag

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
