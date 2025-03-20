import cv2

img1 = cv2.imread("/pizza.jpg")
if img1 is None:
    print("Error: Unable to load image")
else:
    print("Image loaded successfully")
