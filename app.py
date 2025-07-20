from fpdf import FPDF
from datetime import datetime

def generer_devis(nom_client, prestation, montant):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="DEVIS", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Client : {nom_client}", ln=2)
    pdf.cell(200, 10, txt=f"Prestation : {prestation}", ln=3)
    pdf.cell(200, 10, txt=f"Montant : {montant} EUR TTC", ln=4)
    pdf.cell(200, 10, txt=f"Date : {datetime.today().strftime('%d/%m/%Y')}", ln=5)
    pdf.output("devis.pdf")

# Exemple
generer_devis("Monsieur Dupont", "Article SEO 500 mots", 80)
