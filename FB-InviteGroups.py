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

def remove_grupos_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def main():
	# Define o estilo do Graph
	Graph = Figlet(font='slant')
	
	# Define o que vai aparecer no Graph
	GraphRender = Graph.renderText("FacebookBot")
	
	# Limpa a tela antes de executar o Script
	os.system('clear')

	# Mostra o Graph
	print("%s" % (backgroundColor.OKBLUE + backgroundColor.BOLD + GraphRender + backgroundColor.ENDC))
	print(backgroundColor.FAIL + "\rAutomatização de participação nos grupos do Facebook.\nNão me responsabilizo por possíveis Bloqueios." + backgroundColor.OKBLUE + backgroundColor.BOLD + "\nBy Nícolas Pastorello (https://github.com/nicopastorello)\n" + backgroundColor.ENDC)

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

	# Espera 5 segundos
	time.sleep(5)

	# Informa que está fazendo o login no Facebook
	print(backgroundColor.WARNING + "\r[!] Fazendo login no Facebook." + backgroundColor.ENDC)

	# Verifica se fez login no Facebook
	try:
		driver.find_element(By.XPATH,"//input[@value='OK']").click()
		# Informa que esta logado no Facebook
		print(backgroundColor.OKGREEN + "\r[+] Logado no Facebook.\n" + backgroundColor.ENDC)
	except NoSuchElementException:
		print(backgroundColor.FAIL + "\r[-] Erro: O e-mail ou senha que você inseriu está incorreta." + backgroundColor.ENDC)
		finalizar()

	# Espera 5 segundos
	time.sleep(5)

	# Lista dos Grupos do Facebook
	lista_grupos = [
		"https://mbasic.facebook.com/groups/000000001/",
		"https://mbasic.facebook.com/groups/000000002/",
		"https://mbasic.facebook.com/groups/000000003/",
		"https://mbasic.facebook.com/groups/000000004/"
	]

	# Informa que vai iniciar a participar nos grupos da lista
	print(backgroundColor.OKGREEN + "\r[!] Iniciando a participar nos Grupos do Facebook.\n" + backgroundColor.ENDC)

	for grupos in lista_grupos:

		# Acessa o grupo do Facebook
		driver.get(grupos)

		# Espera a pagina ser carregada se a internet estiver lenta
		espera = driver.set_page_load_timeout(60 * 50)

		# Pega o nome do Grupo do Facebook que está acessando.
		nome_grupo = driver.title

		# Informa qual grupo foi acessado 
		print(backgroundColor.OKGREEN + "\r[+] Acessando o grupo : " + backgroundColor.OKGREEN + backgroundColor.BOLD + nome_grupo + backgroundColor.ENDC)
			
		# Espera a pagina ser carregada se a internet estiver lenta
		espera = driver.set_page_load_timeout(60 * 50)

		# Clica em 'Participar do grupo'
		try:
			driver.find_element(By.XPATH,"//input[@value='Participar do grupo']").click()
			print(backgroundColor.WARNING + "\r[!] Participado do grupo." + backgroundColor.ENDC)
		except NoSuchElementException:
			# Informa que já participa
			print(backgroundColor.FAIL + "\r[-] Erro: Vocẽ já participa neste grupo." + backgroundColor.ENDC)

		# Informa que foi finalizado no grupo
		print(backgroundColor.OKGREEN + "\r[+] Finalizando no grupo.\n" + backgroundColor.ENDC)
		

	# Fechar navegador
	driver.quit()

if __name__ == "__main__" :
	main()
	finalizar()
