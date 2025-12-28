import cv2

# opencv and numpy are closely related to each other
# opencv extract pixels from image and loads it into numpy array

img = cv2.imread("assets/Picture81.jpg", -1)

# print(type(img))

print(img.shape)  # (225, 225, 3) : (heigth, width, channel(represents color space))

# opencv uses color: BGR (0-255)
[[[0, 0, 0], [255, 255, 255]], [[0, 0, 0], [255, 255, 255]]]
