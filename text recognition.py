import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"E:\Tesseract\Install Tesseract\tesseract.exe" #Lokasi program

img = cv2.imread("Gambar2.png") #Pengambilan gambar - library opencv

#Image Preprocessing

#Pengaturan ukuran gambar
img = cv2.resize(img, None, fx=1, fy=1) 

#Mengkonversi warna gambar menjadi grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Mengkonversi warna gambar menjadi hitam-putih (menggunakan adaptive threshold)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 3" #konversi teks pada gambar menjadi teks format string - library pyetesseract - Output program
text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
print(text)

#Menampilkan gambar

cv2.imshow("before", gray) #Program before
cv2.imshow("after", adaptive_threshold) #Program after
cv2.waitKey(0)