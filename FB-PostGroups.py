#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pyfiglet import Figlet

import os, sys, time, getpass

class backgroundColor:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def finalizar():
	# Mata o processo do navegador
	os.system("killall -9 firefox")

	# Informa que foi fechado o navegador
	print(backgroundColor.OKGREEN + "\r[+] Fechado o navegador." + backgroundColor.ENDC)

	# Verifica se existe o arquivo de log
	if os.path.exists("geckodriver.log"):
	    # Deleta o arquivo de log 
	    os.remove("geckodriver.log")

	# Informa que foi finalizado o script
	print(backgroundColor.WARNING + "\r[!] Script finalizado." + backgroundColor.ENDC)

	# Finaliza o Script
	sys.exit()

def main():
	# Define o estilo do Graph
	Graph = Figlet(font='slant')
	
	# Define o que vai aparecer no Graph
	GraphRender = Graph.renderText("FacebookBot")
	
	# Limpa a tela antes de executar o Script
	os.system('clear')

	# Mostra o Graph
	print("%s" % (backgroundColor.OKBLUE + backgroundColor.BOLD + GraphRender + backgroundColor.ENDC))
	print(backgroundColor.FAIL + "\rAutomatização de postagem em grupos do Facebook.\nNão me responsabilizo por possíveis Bloqueios." + backgroundColor.OKBLUE + backgroundColor.BOLD + "\nBy Nícolas Pastorello (https://github.com/nicopastorello)\n" + backgroundColor.ENDC)

	# Informa que está sendo iniciado o Script
	print(backgroundColor.WARNING + "\r[!] Iniciando o Script com sucesso." + backgroundColor.ENDC)

	# Solicita a senha do Facebook
	chave = getpass.getpass(backgroundColor.WARNING + "\r[!] Informe sua senha do Facebook : " + backgroundColor.ENDC)

	# Criar instância do navegador
	driver = webdriver.Firefox()

	# Minimiza a janela do navegador.
	driver.minimize_window()

	# Acessa a página de login do Facebook
	driver.get("https://mbasic.facebook.com")

	# Informa que está acessando o Facebook
	print(backgroundColor.WARNING + "\r[!] Fazendo acesso no Facebook." + backgroundColor.ENDC)

	# Encontrar elemento do campo de e-mail pelo atributo
	email = driver.find_element_by_name("email")

	# Digita o e-mail no campo de e-mail pelo atributo
	email.send_keys("SEU E-MAIL AQUI")

	# Encontrar elemento do campo de senha pelo atributo
	senha = driver.find_element_by_name("pass")

	# Digita a senha no campo de senha pelo atributo
	senha.send_keys(chave)

	# Simular que o enter seja precisonado
	senha = driver.find_element_by_name("pass").send_keys(Keys.ENTER)

	# Informa que está fazendo o login no Facebook
	print(backgroundColor.WARNING + "\r[!] Fazendo login no Facebook." + backgroundColor.ENDC)

	# Espera 5 segundos
	time.sleep(5)

	# Ativa a opção de ter imagem
	com_imagem = True # True ou False

	# Caminho onde está a imagem
	caminho_imagem = "/home/nicolas/Downloads/teste.png"

	# Lista dos Grupos do Facebook
	lista_grupos = [
		"https://mbasic.facebook.com/groups/bento.brik/",
		"https://mbasic.facebook.com/groups/bento.ofertas/",
		"https://mbasic.facebook.com/groups/carimbaqueetopcx/",
		"https://mbasic.facebook.com/groups/desapegabg/",
		"https://mbasic.facebook.com/groups/126654534210549/",
		"https://mbasic.facebook.com/groups/1459711954270466/",
		"https://mbasic.facebook.com/groups/sobrikebg/",
		"https://mbasic.facebook.com/groups/1156621451019611/",
		"https://mbasic.facebook.com/groups/1383351131903410/",
		"https://mbasic.facebook.com/groups/tratofeitoserra/",
		"https://mbasic.facebook.com/groups/1500074506917106/",
		"https://mbasic.facebook.com/groups/1523832431209344/",
		"https://mbasic.facebook.com/groups/1639117106331699/",
		"https://mbasic.facebook.com/groups/1582019808750961/",
		"https://mbasic.facebook.com/groups/258201714291546/",
		"https://mbasic.facebook.com/groups/749825018361273/",
		"https://mbasic.facebook.com/groups/brechochiccaxias/",
		"https://mbasic.facebook.com/groups/613777732097033/",
		"https://mbasic.facebook.com/groups/607495159274855/",
		"https://mbasic.facebook.com/groups/598851003589202/",
		"https://mbasic.facebook.com/groups/596555923695970/",
		"https://mbasic.facebook.com/groups/581288991887502/",
		"https://mbasic.facebook.com/groups/524117857681736/",
		"https://mbasic.facebook.com/groups/BrechoMasculinocxs/",
		"https://mbasic.facebook.com/groups/469633646536045/",
		"https://mbasic.facebook.com/groups/FaceBrickCaxias/",
		"https://mbasic.facebook.com/groups/395554883848795/",
		"https://mbasic.facebook.com/groups/393549894043627/",
		"https://mbasic.facebook.com/groups/343172739211759/",
		"https://mbasic.facebook.com/groups/340154489447409/",
		"https://mbasic.facebook.com/groups/307770416239580/",
		"https://mbasic.facebook.com/groups/294998417278124/",
		"https://mbasic.facebook.com/groups/naoserve/",
		"https://mbasic.facebook.com/groups/EnjoeiCaxiasDoSul/",
		"https://mbasic.facebook.com/groups/383826408411478/",
		"https://mbasic.facebook.com/groups/1509753202620575/",
		"https://mbasic.facebook.com/groups/545060655622919/",
		"https://mbasic.facebook.com/groups/492698777546546/",
		"https://mbasic.facebook.com/groups/sebobg/",
		"https://mbasic.facebook.com/groups/1450405745237103/",
		"https://mbasic.facebook.com/groups/275768365965477/",
		"https://mbasic.facebook.com/groups/718327341606318/",
		"https://mbasic.facebook.com/groups/545060655622919/",
		"https://mbasic.facebook.com/groups/negocioscxs/",
		"https://mbasic.facebook.com/groups/374688152720174/",
		"https://mbasic.facebook.com/groups/522436421150725/",
		"https://mbasic.facebook.com/groups/725228584202844/",
		"https://mbasic.facebook.com/groups/996328937079195/",
		"https://mbasic.facebook.com/groups/646742192132000/",
		"https://mbasic.facebook.com/groups/NEGOCIOSDASERRA/",
		"https://mbasic.facebook.com/groups/Briknaserra/",
		"https://mbasic.facebook.com/groups/desapegaa/",
		"https://mbasic.facebook.com/groups/Vendendobentogoncalves/"
	]

	# Informa que vai iniciar a postagem nos grupos da lista
	print(backgroundColor.OKGREEN + "\r[!] Iniciando a postagem nos Grupos do Facebook.\n" + backgroundColor.ENDC)

	for grupos in lista_grupos:

		# Acessa o grupo do Facebook
		driver.get(grupos)

		# Espera a pagina ser carregada se a internet estiver lenta
		espera = driver.set_page_load_timeout(60 * 5)

		try:
			# Pega o nome do Grupo do Facebook que está acessando.
			nome_grupo = driver.title

			# Informa qual grupo foi acessado 
			print(backgroundColor.OKGREEN + "\r[+] Acessando o grupo : " + backgroundColor.OKGREEN + backgroundColor.BOLD + nome_grupo + backgroundColor.ENDC)

			# Encontrar elemento do campo de postagem pelo atributo
			caixa_mensagem = driver.find_element_by_name("xc_message")

			# Informa que vai ser iniciado a postagem no Grupo
			print(backgroundColor.WARNING + "\r[!] Iniciado a postagem no grupo." + backgroundColor.ENDC)
			
			# Digita a mensagem no campo de postagem pelo atributo
			caixa_mensagem.send_keys(u"Teste de um script em Selenium para postar em Grupos do Facebook!")

			# Informa que está sendo postado a mensagem
			print(backgroundColor.OKGREEN + "\r[+] Adicionando a mensagem na postagem." + backgroundColor.ENDC)

			# Verifica se existe a imagem 
			if os.path.exists(caminho_imagem):
				# Adiciona uma imagem se estiver ativada
				if com_imagem:
					# Espera a pagina ser carregada se a internet estiver lenta
					espera = driver.set_page_load_timeout(60 * 5)
					
					# Encontrar elemento do campo de foto pelo atributo e clica
					add_imagem = driver.find_element_by_name("view_photo").click()

					# Realiza o upload da imagem pelo 'caminho_imagem'
					driver.find_element_by_name("file1").send_keys(caminho_imagem)

					# Espera a pagina ser carregada se a internet estiver lenta
					espera = driver.set_page_load_timeout(60 * 5)

					# Adiciona a imagem a postagem
					driver.find_element_by_name("add_photo_done").click()

					# Informa que está sendo adicionando a imagem na postagem
					print(backgroundColor.OKGREEN + "\r[+] Adicionando a imagem na postagem." + backgroundColor.ENDC)
				else:
				 	print(backgroundColor.FAIL + "\r[-] Imagem não está ativada." + backgroundColor.ENDC)
			else:
				# Informa que a imagem não encontrada
				print(backgroundColor.FAIL + "\r[-] Erro: Imagem não encontrada." + backgroundColor.ENDC)
				
				# Finaliza o Script
				finalizar()
				
			# Espera a pagina ser carregada se a internet estiver lenta
			espera = driver.set_page_load_timeout(60 * 5)

			# Encontrar elemento do campo de publicar pelo atributo
			publicar = driver.find_element_by_name("view_post").click()

			# Clica em Concluir somente quando está com uma imagem
			if com_imagem:
				# Encontrar elemento do campo de concluir pelo atributo
				finaliza = driver.find_element_by_name("done").click()
			
			# Informa que foi finalizado no grupo que está sendo postado
			print(backgroundColor.OKGREEN + "\r[+] Finalizando a postagem no grupo.\n" + backgroundColor.ENDC)
		except NoSuchElementException:
			print(backgroundColor.FAIL + "\r[-] Erro: " + backgroundColor.ENDC)
		
		# Espera 5 segundos
		time.sleep(5)

	# Fechar navegador
	driver.quit()

if __name__ == "__main__" :
	main()
	finalizar()
