from fpdf import FPDF
from datetime import datetime

class DevisPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Devis Freelance', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_devis(self, client, prestation, prix):
        self.set_font('Arial', '', 12)
        self.ln(10)
        self.cell(0, 10, f"Client : {client}", ln=True)
        self.cell(0, 10, f"Prestation : {prestation}", ln=True)
        self.cell(0, 10, f"Prix : {prix} €", ln=True)
        self.cell(0, 10, f"Date : {datetime.today().strftime('%d/%m/%Y')}", ln=True)

if __name__ == "__main__":
    pdf = DevisPDF()
    pdf.add_page()
    pdf.add_devis("Monsieur Dupont", "Article SEO 500 mots", "75")
    pdf.output("devis_dupont.pdf")
