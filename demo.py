import cv2

img = cv2.imread("assets/Picture81.jpg", 1)

"""
-1, cv2.IMREAD_COLOR : loads a color image. any transparency of image will be neglected. It is the default flag.
0, cv2.IMREAD_GRAYSCALE : loads image in gray scale mode
1, cv2.IMREAD_UNCHANGED : loads image as such including alpha channel (transparent image)
"""

cv2.imshow("Fish Image", img)
cv2.waitKey(0)  # will wait infinitly until you press any key on window
cv2.destroyAllWindows()
