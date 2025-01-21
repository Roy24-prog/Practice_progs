import cv2
import easyocr
import pandas as pd

image_path = r'D:\Pyproj\Img_to_text\Caption.jpg'

img = cv2.imread(image_path)
reader = easyocr.Reader(['en'], gpu=True)

text_data = reader.readtext(img)


df = pd.DataFrame(text_data)

text_ = df[1].tolist()
print(*text_)


input("Press over...")  