import subprocess
import os

# Paths to your CV .qmd files
cv_qmd_files = {
    'en': 'cv/cv_en.qmd',
    'es': 'cv/cv_es.qmd',
    'pt': 'cv/cv_pt.qmd'
}

# Output paths for the CVs
output_paths = {
    'html': {
        'en': 'cv/cv_en.html',
        'es': 'cv/cv_es.html',
        'pt': 'cv/cv_pt.html'
    },
    'pdf': {
        'en': 'cv/cv_en.pdf',
        'es': 'cv/cv_es.pdf',
        'pt': 'cv/cv_pt.pdf'
    }
}

# Path to wkhtmltopdf
wkhtmltopdf_path = '/usr/bin/wkhtmltopdf'  # Atualize para o caminho correto

# Generate HTML and PDF for each language
for lang, qmd_file in cv_qmd_files.items():
    # Verificar se o arquivo .qmd existe
    if not os.path.exists(qmd_file):
        print(f"Arquivo {qmd_file} não encontrado.")
        continue
    
    # Renderizar o arquivo .qmd para HTML
    subprocess.run(['quarto', 'render', qmd_file])
    
    # Caminho do arquivo HTML gerado
    html_path = output_paths['html'][lang]
    
    # Verificar se o HTML foi gerado
    if not os.path.exists(html_path):
        print(f"HTML {html_path} não foi gerado.")
        continue

    # Converter HTML para PDF
    pdf_path = output_paths['pdf'][lang]
    subprocess.run([wkhtmltopdf_path, html_path, pdf_path])

print("CVs gerados e convertidos para PDF com sucesso.")
