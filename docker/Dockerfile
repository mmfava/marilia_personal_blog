# Use a imagem base do Jupyter Notebook
FROM jupyter/base-notebook:python-3.10.11

# Trocar para o usuário root para a instalação
USER root

# Criar diretório com permissões adequadas
RUN mkdir -p /home/jovyan/opt

# Instalar Quarto
RUN apt-get update \ 
    && wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.5.54/quarto-1.5.54-linux-amd64.tar.gz \
    && tar -xvzf quarto-1.5.54-linux-amd64.tar.gz \
    && mv quarto-1.5.54 /home/jovyan/opt/quarto-1.5.54 \
    && ln -s /home/jovyan/opt/quarto-1.5.54/bin/quarto /usr/local/bin/quarto

# Instalar Pandoc
RUN quarto install tinytex

# Permitir uso de sudo sem senha
RUN echo "jovyan ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Copiar arquivos do projeto para o container
COPY . /home/jovyan/work

# Verificar instalações
RUN quarto check

# Comando para iniciar o Jupyter Notebook
CMD ["start-notebook.sh"]