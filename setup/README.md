# Diretório setup

Este diretório contém scripts auxiliares para configurar o ambiente e facilitar o fluxo de trabalho com Quarto neste projeto.

## Scripts disponíveis

### criar_post.py

Script em Python para criar um novo conteúdo (post, experiment, talk, etc.) no formato Quarto. O script gera um diretório com o prefixo de data e um slug baseado no título, contendo um arquivo `sobre.qmd` com front matter YAML.

Uso:
```bash
python setup/criar_post.py "Título do post" [-c categoria] [-d YYYY-MM-DD]
```

Parâmetros:
- `titulo`: Título do post (entre aspas).
- `-c, --categoria`: Categoria do conteúdo (padrão: `posts`). Valores válidos: `posts`, `experiments`, `talks-teaching`, `academic`.
- `-d, --data`: Data no formato `YYYY-MM-DD` (padrão: data atual).

### quarto.sh

Script em Bash para verificar e instalar o comando `uv` e, em seguida, baixar e instalar o Quarto CLI em sistemas baseados em Debian/Ubuntu.

Uso:
```bash
cd setup
bash quarto.sh
```

O script executa:
1. Verificação e instalação do pacote `uv` (se não estiver instalado).
2. Download do arquivo `.deb` do Quarto (versão fixa definida no script).
3. Instalação do Quarto via `dpkg` e correção de dependências com `apt-get`.
4. Verificação final da instalação com `quarto check`.

### normalize_categories.py

Script em Python para padronar todas as entradas de `categories:` em arquivos Quarto (`.qmd`) para caixa baixa. Percorre os diretórios de conteúdo e ajusta o front matter YAML.

Uso:
```bash
python setup/normalize_categories.py
```