# -*- coding: UTF-8 -*-

#Este é um teste de um programa que renomea pastas e arquivos retirando caracteres especiais
# Diretorio teste: /Users/bruno/Desktop/DirTeste

import os, sys, shutil

caminho_atual = raw_input("Insira o caminho do diretorio: ")

print "Varrendo Caminho: " + caminho_atual

diretorio = os.walk(caminho_atual)
diretorio_espelho = []
#Adiciona os caminhos em um espelho para renomear depois
for subdir in diretorio:
    diretorio_espelho.append(str(subdir[0]))
#Teste para printar diretorios
for pasta in diretorio_espelho:
    print pasta