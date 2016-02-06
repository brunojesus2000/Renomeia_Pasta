# -*- coding: UTF-8 -*-

#Este é um teste de um programa que renomea pastas e arquivos retirando caracteres especiais
# Diretorio teste: /Users/bruno/Desktop/Faculdade2

import os, sys, shutil, string


caminho_atual = "/Users/bruno.paixao/Desktop/DirTeste"

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


cont_list = len(diretorio_espelho)
cont_dir = 0
cont_items = 0

#Teste para printar diretorios
for pasta in range(cont_list):
	if (pasta == 0) or (pasta == cont_dir):

		print True
	else:
		cont_dir += 1
		pasta_old = diretorio_espelho[pasta]
		pasta_new = pasta_old.translate(None, 'ã\'$\"*çé́?̃\%_-^̂' )
		print pasta_old + " indo para " + pasta_new
		os.rename(pasta_old, pasta_new)
		diretorio_espelho = varre_diretorio(caminho_atual)
		print pasta_old + " == " + pasta_new

#Teste para renomear arquivos
for pasta in os.walk(caminho_atual):
	for item in pasta[2]:
		cont_items += 1
		item_old = pasta[0] + "/" + str(item)
		item_new = item_old.translate(None, 'ã\'$\"*çé́?̃\%_-^̂' )
		print item_old + " indo para " + item_new
		os.rename(item_old, item_new)
		print item_old + " == " + item_new

print "____________________________________________________________________________________"
print "Finalizado com sucesso!"
print "Foram varridos:"
print "%d diretorios e %d arquivos" % (cont_dir,cont_items)
print "____________________________________________________________________________________"