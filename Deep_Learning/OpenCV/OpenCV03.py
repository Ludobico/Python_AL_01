import cv2

image = cv2.imread('./images/cat.jpg', cv2.IMREAD_ANYCOLOR)
# image = cv2.imread('./images/cat.jpg', cv2.IMREAD_GRAYSCALE) 흑백사진
print(image.shape)
cv2.imshow('img', image)
cv2.waitKey()
cv2.destroyAllWindows()
