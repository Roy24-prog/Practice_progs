import requests
from bs4 import BeautifulSoup
import re


url =  "https://www.acs-college.com/education-in-developing-countries"
           
print("\nExtracting Page", url, ">>>>>>>>>>>>>>\n")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_='et_pb_text_inner') #finding text in class et_pb_text_inner
content = soup.find_all('p')
paragraphs = []

for x in content:
    paragraphs.append(str(x))

print(type(paragraphs))
print("Received content. \nRamoving tags...")

for i in range(len(paragraphs)):
   text = re.sub(r"<.*?>", "", paragraphs[i])
   print(text)
 


    
input("Done! \nPress over...")