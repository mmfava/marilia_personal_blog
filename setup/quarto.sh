#!/bin/bash
# Script para verificar e instalar o uv e, em seguida, instalar o Quarto

# Função para imprimir mensagens com destaque
imprime_mensagem() {
  echo "--------------------------------------------------"
  echo "$1"
  echo "--------------------------------------------------"
}

# 1. Verificar se o comando 'uv' está instalado
if command -v uv >/dev/null 2>&1; then
  imprime_mensagem "O 'uv' já está instalado."
else
  imprime_mensagem "O 'uv' não está instalado. Iniciando instalação..."
  # Atualiza a lista de pacotes
  sudo apt-get update
  # Instala o pacote 'uv'
  sudo apt-get install -y uv
  
  # Verifica se a instalação foi concluída
  if command -v uv >/dev/null 2>&1; then
    imprime_mensagem "'uv' instalado com sucesso."
  else
    imprime_mensagem "Houve um problema ao instalar o 'uv'. Verifique se o pacote existe em seu repositório."
    # Se não encontrar o pacote, o script pode ser interrompido ou continuar.
    # exit 1  # Descomente esta linha se preferir encerrar o script em caso de erro.
  fi
fi

# 2. Instalar o Quarto

# Definir URL e nome do arquivo DEB do Quarto
QUARTO_URL="https://github.com/quarto-dev/quarto-cli/releases/download/v1.7.23/quarto-1.7.23-linux-amd64.deb"
DEB_FILE="quarto-1.7.23-linux-amd64.deb"

imprime_mensagem "Baixando o Quarto..."
wget "$QUARTO_URL" -O "$DEB_FILE"

imprime_mensagem "Instalando o Quarto..."
sudo dpkg -i "$DEB_FILE"

imprime_mensagem "Corrigindo dependências (se necessário)..."
sudo apt-get install -f -y

imprime_mensagem "Verificando a instalação do Quarto..."
quarto check

imprime_mensagem "Processo concluído. Verifique as mensagens acima para confirmar que as instalações ocorreram conforme esperado."
