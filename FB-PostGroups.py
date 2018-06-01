#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, time, getpass

# Informa o tempo de inicio do Script
inicio = time.time()

# Informa que esta sendo iniciado o Script
print "\033[93m - Iniciando o Script."

# Solicita a senha do Facebook
chave = getpass.getpass("033[94m - Informe sua senha do Facebook : ")

# Criar instância do navegador
driver = webdriver.Firefox()

# Minimiza a janela do navegador.
driver.minimize_window()

# Acessa a página de login do Facebook
driver.get("https://mbasic.facebook.com")

# Informa que esta acessando o Facebook
print "\033[94m - Fazendo acesso no Facebook..."

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

# Informa que esta fazendo o login no Facebook
print "\033[94m - Fazendo login no Facebook...\n"

# Espera 5 segundos
time.sleep(5)

# Ativa a opção de ter imagem
com_imagem = True # True ou False

# Caminho onde está a imagem
caminho_imagem = "/home/nicolas/Downloads/teste.png"

# Lista dos Grupos do Facebook
links_grupos = [
	"https://mbasic.facebook.com/groups/000000001/",
	"https://mbasic.facebook.com/groups/000000002/",
	"https://mbasic.facebook.com/groups/000000003/",
	"https://mbasic.facebook.com/groups/000000004/",
]

for grupos in links_grupos:

	# Acessa o grupo do Facebook
	driver.get(grupos)

	# Pega o nome do Grupo do Facebook que esta acessando.
	nome_grupo = driver.title

	# Informa qual grupo foi acessado 
	print "\033[1m\033[94m - Acessando o grupo\033[1m\033[35m", nome_grupo

	# Encontrar elemento do campo de postagem pelo atributo
	caixa_mensagem = driver.find_element_by_name("xc_message")

	# Informa que vai ser iniciado a postagem no Grupo
	print "\033[92m - Iniciado a postagem no grupo."
	
	# Digita a mensagem no campo de postagem pelo atributo
	caixa_mensagem.send_keys(u"Teste de um script em Selenium incrível para postar em grupos do Facebook!\nBy Nicolas Pastorello")

	# Informa que esta sendo postado a mensagem
	print "\033[92m - Adicionando a mensagem na postagem."

	# Adiciona uma imagem
	if com_imagem:
		# Encontrar elemento do campo de foto pelo atributo e clica
		add_imagem = driver.find_element_by_name("view_photo").click()

		# Realiza o upload da imagem pelo 'caminho_imagem'
		driver.find_element_by_name("file1").send_keys(caminho_imagem)

		# Adiciona a imagem a postagem
		driver.find_element_by_name("add_photo_done").click()

		# Informa que esta sendo adicionando a imagem na postagem
		print "\033[92m - Adicionando a imagem na postagem."
		
	# Espera a pagina ser carregada se a internet estiver lenta
	espera = driver.set_page_load_timeout(60 * 5)

	# Encontrar elemento do campo de publicar pelo atributo
	publicar = driver.find_element_by_name("view_post").click()

	# Clica em Concluir somente quando esta com uma imagem.
	if com_imagem:
		# Encontrar elemento do campo de concluir pelo atributo
		finaliza = driver.find_element_by_name("done").click()
	
	# Pega o nome do Grupo que esta sendo postado
	print "\033[1m\033[92m - Finalizando a postagem no grupo.\x1b[0m\n\n"
	
	# Espera 5 segundos
	time.sleep(5)

# Fechar navegador
driver.quit()

# Informa o tempo de final do Script
final = time.time()

# Calcula o tempo de final menos o tempo de inicio
calcula = final - inicio

print "\033[93m - Tempo de execução :",calcula

# Informa que foi fechado o navegador
print "\033[93m - Fechado o navegador."

# Verifica se existe o arquivo de log
if os.path.exists("geckodriver.log"):
    # Deleta o arquivo de log 
    os.remove("geckodriver.log")

# Informa que foi finalizado o script
print "\033[93m - Script finalizado."
