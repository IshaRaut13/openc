import cv2

img = cv2.imread("assets/Picture81.jpg", 0)
img = cv2.resize(img, (300, 300))  # this is if you want to do by pixels
img = cv2.resize(img, (0, 0), fx=2, fy=2)  # if you want 1/3 image somewhat like that
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("assets/new_img.jpg", img)  # filename in which this img is stored

cv2.imshow("Fish Image", img)
cv2.waitKey(0)  # will wait infinitly until you press any key on window
cv2.destroyAllWindows()
