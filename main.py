from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello Everyone !", align="L", ln=1)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="I am Anand, Nice to meet you :)", align="L", ln=1)

pdf.output("Output.pdf")