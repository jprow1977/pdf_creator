from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
# create dataframe
df = pd.read_csv("topics.csv")
print(df)

for index, row in df.iterrows():
    pdf.set_font("Times", "B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.add_page()
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)


    # set footer
    pdf.ln(265)
    pdf.set_font(family="Times", style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # set footer
        pdf.ln(277)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output('output.pdf')
