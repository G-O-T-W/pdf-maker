from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Add header page
    pdf.add_page()

    pdf.set_font("Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align="l")
    pdf.line(10, 22, 200, 22)

    # Add extra pages
    extra_page = row['Pages'] - 1
    for i in range(extra_page):
        pdf.add_page()

# Create pdf
pdf.output("output.pdf")