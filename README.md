# 🧾 Générateur de Devis PDF

Ce script Python permet de générer automatiquement un fichier PDF pour un devis.

## ⚙️ Fonctionnalités

- Génère un fichier PDF avec :
  - Nom du client
  - Description de la prestation
  - Montant à facturer
  - Date du jour
- Format propre, clair, lisible
- Facile à modifier

## 🛠️ Librairies utilisées

- `fpdf` : création de fichiers PDF
- `datetime` : gestion des dates

## ▶️ Exemple d'utilisation

```python
generer_devis("Monsieur Dupont", "Article SEO 500 mots", 80)
