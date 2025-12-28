import cv2

img = cv2.imread("assets/Picture81.jpg", 0)
img = cv2.resize(img, (300, 300))  # this is if you want to do by pixels
img = cv2.resize(img, (0, 0), fx=5, fy=2.5)  # if you want 1/3 image somewhat like that

cv2.imshow("Fish Image", img)
cv2.waitKey(0)  # will wait infinitly until you press any key on window
cv2.destroyAllWindows()
