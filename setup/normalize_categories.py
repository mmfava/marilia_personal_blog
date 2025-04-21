#!/usr/bin/env python3
"""
Script para padronizar as categorias em front matter YAML para lowercase.

Percorre todos os arquivos `.qmd` nos diretórios de conteúdo e converte
os valores da lista `categories:` para caixa baixa, evitando redundância.

Uso:
    python setup/normalize_categories.py
"""
import os
import re

def normalize_file(path):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    out_lines = []
    in_front_matter = False
    in_categories_block = False
    for line in lines:
        # Detectar início/fim do front matter YAML
        if re.match(r'^---\s*$', line):
            # alternar estado e resetar bloco de categorias
            if not in_front_matter:
                in_front_matter = True
            else:
                in_front_matter = False
            in_categories_block = False
            out_lines.append(line)
            continue
        # Se dentro do front matter
        if in_front_matter:
            # Detectar início da chave categories
            if re.match(r'^\s*categories\s*:\s*$', line):
                in_categories_block = True
                out_lines.append(line)
                continue
            # Processar itens de categoria
            if in_categories_block and re.match(r'^\s*-\s+', line):
                prefix, value = line.split('-', 1)
                # converter valor para lowercase e preservar indentação
                new_val = value.lower()
                out_lines.append(f"{prefix}-{new_val}")
                continue
            # Se encontrar outra chave ou encerrar listas, sair do bloco
            if in_categories_block and re.match(r'^[^ \t-]', line):
                in_categories_block = False
        out_lines.append(line)
    # Sobrescrever arquivo apenas se houve mudança
    if out_lines != lines:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)

def main():
    # Diretórios de conteúdo Quarto
    dirs = ['posts', 'experiments', 'talks-teaching', 'academic']
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for root, _, files in os.walk(d):
            for fname in files:
                if fname.endswith('.qmd'):
                    filepath = os.path.join(root, fname)
                    normalize_file(filepath)
    print('✅ Categorias normalizadas para lowercase em todos os front matter (.qmd)')

if __name__ == '__main__':
    main()