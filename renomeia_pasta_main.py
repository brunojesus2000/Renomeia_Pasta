# -*- coding: UTF-8 -*-

#Este é um teste de um programa que renomea pastas e arquivos retirando caracteres especiais
# Diretorio teste: /Users/bruno/Desktop/Faculdade2

import os, sys, shutil


caminho_atual = "/Users/bruno/Desktop/DirTeste"

print "Varrendo Caminho: " + caminho_atual

diretorio = os.walk(caminho_atual)
diretorio_espelho = []
#Adiciona os caminhos em um espelho para renomear depois
def varre_diretorio(dir_atual):
	dir_espelho = []
	for subdir in os.walk(dir_atual):
	    dir_espelho.append(str(subdir[0]))
	return dir_espelho

diretorio_espelho = varre_diretorio(caminho_atual)

cont_dir = len(diretorio_espelho)
print cont_dir


#Teste para printar diretorios
for pasta in range(cont_dir):
	if (pasta == 0) or (pasta == cont_dir):

		print True
	else:

		pasta_old = diretorio_espelho[pasta]
		pasta_new = (diretorio_espelho[pasta] + str(pasta))
		print pasta_old + " indo para " + pasta_new
		os.rename(pasta_old, pasta_new)
		diretorio_espelho = varre_diretorio(caminho_atual)
		print pasta_old + " == " + pasta_new
