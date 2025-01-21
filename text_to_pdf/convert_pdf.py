
from fpdf import FPDF
  
# save FPDF() class into 

# a variable pdf
pdf = FPDF()   
  
# Add a page
pdf.add_page()
  
# set style and size of font 
# that you want in the pdf
pdf.set_font("Arial", size = 15)
 
# open the text file in read mode
f = open("D:\\Pyproj\\text_to_pdf\\Class_6th.txt", "r")
 
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
  
# save the pdf with name .pdf
out_path = "D:\\Pyproj\\text_to_pdf\\Class_6th.pdf"
pdf.output(out_path)  