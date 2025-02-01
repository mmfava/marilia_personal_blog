# Meu blog pessoal

[www.mariliafavalesso.com](www.mariliafavalesso.com) <br>

Este repositório contém o código-fonte do meu blog pessoal, construído com [Quarto 1.5.54](https://quarto.org/) e desenvolvido em um container Jupyter baseado na imagem [jupyter/base-notebook](https://hub.docker.com/r/jupyter/base-notebook/). Aqui, compartilho materiais sobre ciência de dados, modelagem, análises avançadas, programação e ecoepidemiologia.

## Deploy

O blog é implantado automaticamente no Netlify a partir deste repositório. 
Cada push no branch principal aciona uma nova implantação (ver [netlify.toml](netlify.toml)).

## Pré-requisitos

### Instalar o quarto 1.5.54

```{bash}
# Instalar Quarto
wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.5.54/quarto-1.5.54-linux-amd64.tar.gz
tar -xvzf quarto-1.5.54-linux-amd64.tar.gz
mkdir -p $HOME/opt
mv quarto-1.5.54 $HOME/opt/quarto-1.5.54
export PATH=$PATH:$HOME/opt/quarto-1.5.54/bin

# Instalar Pandoc
wget https://github.com/jgm/pandoc/releases/download/3.2.0/pandoc-3.2.0-linux-amd64.tar.gz
tar -xvzf pandoc-3.2.0-linux-amd64.tar.gz
sudo mv pandoc-3.2.0/bin/* /usr/local/bin/

# Instalar Dart Sass
wget https://github.com/sass/dart-sass/releases/download/1.70.0/dart-sass-1.70.0-linux-amd64.tar.gz
tar -xvzf dart-sass-1.70.0-linux-amd64.tar.gz
sudo mv dart-sass-1.70.0/* /usr/local/bin/

# Instalar Deno
curl -fsSL https://deno.land/x/install/install.sh | sh
export DENO_INSTALL="$HOME/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"

# Instalar Typst
wget https://github.com/typst/typst/releases/download/v0.11.0/typst-linux-x86_64.zip
unzip typst-linux-x86_64.zip
sudo mv typst /usr/local/bin/

# Instalar TinyTeX
curl -sL "https://yihui.org/tinytex/install-unx.sh" | sh
export PATH=$PATH:$HOME/.TinyTeX/bin/x86_64-linux

# Instalar Python e Jupyter
sudo apt-get update
sudo apt-get install -y python3 python3-pip
pip3 install jupyter

# Instalar R e pacotes
sudo apt-get install -y r-base
R -e "install.packages(c('knitr', 'rmarkdown'), repos='https://cloud.r-project.org/')"
```

### Dependências-do-quarto

```{bash}
pip install chromium

``` 

