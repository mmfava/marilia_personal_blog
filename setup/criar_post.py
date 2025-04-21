import os
from datetime import date
import argparse
import textwrap

AUTOR = {
    "name": "Marília Melo Favalesso",
    "email": "marilia.melo.favalesso@gmail.com"
}

CATEGORIAS_DISPONIVEIS = ["posts", "experiments", "talks-teaching", "academic"]

import unicodedata
import re

def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text)
    return text.lower().strip().replace(" ", "-").replace("/", "-")

def criar_post(titulo, categoria="posts", data=None):
    if categoria not in CATEGORIAS_DISPONIVEIS:
        raise ValueError(f"Categoria inválida. Use uma destas: {', '.join(CATEGORIAS_DISPONIVEIS)}")

    data = data or str(date.today())
    slug = slugify(titulo)
    nome_diretorio = f"{data}-{slug}"
    caminho = os.path.join(categoria, nome_diretorio)
    os.makedirs(caminho, exist_ok=True)

    yaml = textwrap.dedent(f"""\
    ---
    title: "{titulo}"
    date: {data}
    author:
      - name: "{AUTOR['name']}"
        email: "{AUTOR['email']}"
    categories: [{categoria}]
    lang: pt-br
    tags: [PT-BR]
    ---
    """)

    caminho_arquivo = os.path.join(caminho, "sobre.qmd")
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(yaml)

    print(f"✅ Post criado: {caminho_arquivo}")
    return caminho_arquivo


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Cria novo conteúdo Quarto (post, experiment, talk etc.) no projeto"
    )
    parser.add_argument("titulo", help="Título do post entre aspas")
    parser.add_argument(
        "-c", "--categoria",
        default="posts",
        help=(
            "Categoria (default: posts). "  
            "Valores válidos (lowercase): posts, experiments, talks-teaching, academic"
        )
    )
    parser.add_argument("-d", "--data", help="Data no formato YYYY-MM-DD (default: hoje)")

    args = parser.parse_args()

    try:
        criar_post(args.titulo, args.categoria, args.data)
    except Exception as e:
        print("❌ Erro:", e)
