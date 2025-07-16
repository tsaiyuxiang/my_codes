# shirtificate.py
# must   pip installfpdf   first
from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)

# 加入圖片
pdf.image("shirtificate.png", x=0, y=60, w=210)

# 在圖片上加字（位置大約是衣服中央）
pdf.set_xy(0, 120)
pdf.cell(w=210, h=10, txt=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
