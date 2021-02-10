#!/bin/bash

#############################
#    creditos [ghost]
#############################

echo "Instalador"
echo "Serão instalado os seguintes programas"
echo "[Python, Figlet, Toilet, Nmap]"

echo "Instalando python -> pkg install python"
sleep 1

# comando para instalar o python
pkg install python -y

echo "Instalando figlet"
sleep 1

# comando para instalar figlet
pkg install figlet -y

echo "Instalando toilet"
sleep 1

# comando para instalar toilet
pkg install toilet -y

echo "Instalando nmap"
sleep 1

# comando para instalar nmap
pkg install nmap -y

sleep 1

echo -e "\033[32m"
toilet "Instalação"
toilet "Concluida"

echo -e "\033[0;34mScript criado por [GHOST]"
