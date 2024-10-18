from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
# Remove auto page breaks and re-adjust margins
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Add the topic title page
    pdf.add_page()

    # Set the header
    pdf.set_font("Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align="l")

    # Add lines
    for y in range(20, 285, 10):
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font("Times", size=8, style="I")
    pdf.set_text_color(160, 160, 160)
    pdf.cell(w=0, h=4, txt=row['Topic'], align="R")



    # Add extra pages
    extra_page = row['Pages'] - 1
    for i in range(extra_page):
        pdf.add_page()
        # Add lines
        for y in range(20, 285, 10):
            pdf.line(10, y, 200, y)

        # Set the footer
        pdf.ln(277)
        pdf.set_font("Times", size=8, style="I")
        pdf.set_text_color(160, 160, 160)
        pdf.cell(w=0, h=4, txt=row['Topic'], align="R")

# Create pdf
pdf.output("output.pdf")