import cv2

img = cv2.imread("assets/logo.jpg", -1)

print(img[200][40:400])  # [row][pixel range in that row]
print(img[200][400])  # will return one pixel value ([ 40 105 243])
