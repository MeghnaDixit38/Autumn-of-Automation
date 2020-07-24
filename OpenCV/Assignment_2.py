import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/meghnadixit38/Pictures/T.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2) 
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

M = cv2.getRotationMatrix2D((cols/2,rows/2),70,1)
dst = cv2.warpAffine(img,M,(cols,rows)) 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

pts1 = np.float32([[100,100],[230,52],[60,230],[400,400]])
pts2 = np.float32([[100,0],[300,10],[110,300],[300,200]])
M1= cv2.getRotationMatrix2D((cols/2,rows/2),120,10)
dst1 = cv2.warpAffine(img,M,(cols,rows)) 
M = cv2.getPerspectiveTransform(pts1,pts2) 
dst = cv2.warpPerspective(dst1,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

M = cv2.getRotationMatrix2D((cols/2,rows/2),160,2)
dst = cv2.warpAffine(img,M,(cols,rows)) 
blur = cv2.blur(dst,(5,10))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

M = cv2.getRotationMatrix2D((cols/2,rows/2),210,3)
dst = cv2.warpAffine(img,M,(cols,rows)) 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

M = cv2.getRotationMatrix2D((cols/2,rows/2),120,2)
dst = cv2.warpAffine(img,M,(cols,rows)) 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

blur = cv2.blur(img,(10,10))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2) 
dst = cv2.warpPerspective(dst,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

M = cv2.getRotationMatrix2D((cols/6,rows/2),10,2)
dst = cv2.warpAffine(img,M,(cols,rows)) 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

pts1 = np.float32([[300,300],[10,300],[100,10],[200,10]])
pts2 = np.float32([[100,100],[400,100],[100,400],[400,400]])
M = cv2.getPerspectiveTransform(pts1,pts2) 
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()