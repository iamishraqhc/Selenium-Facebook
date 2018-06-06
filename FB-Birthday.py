#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyfiglet import Figlet

import os, sys, time, getpass, random

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
	print(backgroundColor.FAIL + "\rAutomatização de postagem para parabenizar os contatos no Facebook.\nNão me responsabilizo por possíveis Bloqueios." + backgroundColor.OKBLUE + backgroundColor.BOLD + "\nBy Nícolas Pastorello (https://github.com/nicopastorello)\n" + backgroundColor.ENDC)

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

	# Acessa a página de aniversariantes do Facebook
	driver.get("https://www.facebook.com/events/birthdays")

	# Informa que vai iniciar a postagem nos grupos da lista
	print(backgroundColor.OKGREEN + "\r[!] Iniciando a postagem para parabenizar os contatos no Facebook.\n" + backgroundColor.ENDC)

	# Encontrar elemento do campo de mensagem pelo atributo
	aniversariante = driver.find_elements_by_xpath('//*[@class="enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput"]')

	# Lista dos Grupos do Facebook
	lista_mensagens = [
		"Parabéns Tudo de bom e do melhor na sua vida.",
		"Parabéns Tudo do bom e do melhor.",
		"Parabéns Tudo de bom."
	]
	
	# Para cada aniversariante manda os parabens
	for parabens in aniversariante:
		parabens.send_keys(random.choice(lista_mensagens)
		parabens.send_keys(Keys.RETURN)

		# Espera 2 segundos para parabenizar o proximo
		time.sleep(2)

	# Informa que foi finalizado a postagem
	print(backgroundColor.OKGREEN + "\r[+] Finalizando a postagem para parabenizar.\n" + backgroundColor.ENDC)

	# Fechar navegador
	driver.quit()

if __name__ == "__main__" :
	main()
	finalizar()
