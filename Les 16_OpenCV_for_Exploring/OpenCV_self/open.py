import cv2

img = cv2.imread('D:/Learning_5.0_D disk/GeekBrains/BootCamp/Les 16_OpenCV_for_Exploring/OpenCV_self/Berries.jpg')
print(img)
print (img.shape)

img = cv2.resize(img, (500, 500))
print (img.shape)
cv2.imshow('Result', img)

cv2.waitKey(0)