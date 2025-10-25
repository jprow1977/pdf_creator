from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit='mm', format='A4')
# create dataframe
df = pd.read_csv("topics.csv")
print(df)

for index, row in df.iterrows():
    for num in range(row['Pages']):
        pdf.set_font("Times", "B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.add_page()
        pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
        pdf.line(10, 22, 200, 22)

pdf.output('output.pdf')
