import cv2
img=cv2.imread("solor-system.jpg")
cv2.putText(img,"sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(255,255,255))
cv2.putText(img,"mercury",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,0,255))
cv2.putText(img,"venus",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,1,255))
cv2.putText(img,"earth",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,2,255))
cv2.putText(img,"mars",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,3,255))
cv2.putText(img,"jupiter",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,4,255))
cv2.putText(img,"saturn",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,5,255))
cv2.putText(img,"uranus",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,6,255))
cv2.putText(img,"neptune",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,7,255))
cv2.imshow("output",img)
cv2.waitKey(0)