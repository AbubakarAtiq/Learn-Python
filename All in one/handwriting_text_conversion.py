import Flask
import pywhatkit as kit
import cv2
kit.text_to_handwriting("Mohammad Abubakar Atiq",save_to="nametohandwriting.png")
img=cv2.imread("nametohandwriting.png")
cv2.imshow("Text to Handwriting",img)
cv2.waitkey(0)
cv2.destroyAllWindows()