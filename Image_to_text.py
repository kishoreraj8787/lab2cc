from PIL import Image
from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open("C:\\Users\\KRISH\\Desktop\\download.jpg")

text = image_to_string(img, lang="eng")
print(text)
print("Converting image to text")
print("File is converted and saving the file in text file")
file1 = open(r"C:\Users\KRISH\Desktop\output\imageconverted.txt", "a")
file1.writelines(text)
print("Conversion Finished")
file1.close()
