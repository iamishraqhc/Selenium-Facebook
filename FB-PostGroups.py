#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time, getpass

# Solicita a senha do Facebook
chave = getpass.getpass('Informe sua senha : ')

# Criar instância do navegador
driver = webdriver.Firefox()

# Acessa a página de login do Facebook
driver.get('https://mbasic.facebook.com')

# Encontrar elemento do campo de e-mail pelo atributo
email = driver.find_element_by_name("email")

# Digita o e-mail no campo de e-mail pelo atributo
email.send_keys('SEU E-MAIL AQUI')

# Encontrar elemento do campo de senha pelo atributo
senha = driver.find_element_by_name("pass")

# Digita a senha no campo de senha pelo atributo
senha.send_keys(chave)

# Simular que o enter seja precisonado
senha = driver.find_element_by_name("pass").send_keys(Keys.ENTER)

# Espera 5 segundos
time.sleep(5)

# Ativa a opção de ter imagem
com_imagem = True # True ou False

# Caminho onde está a imagem
caminho_imagem = "/home/nicolas/Downloads/teste.png"

# Lista dos Grupos do Facebook
links_grupos = [
	"https://mbasic.facebook.com/groups/bento.brik/",
	"https://mbasic.facebook.com/groups/bento.ofertas/",
]

for grupos in links_grupos:

	# Acessa o grupo do Facebook
	driver.get(grupos)

	# Encontrar elemento do campo de postagem pelo atributo
	caixa_mensagem = driver.find_element_by_name("xc_message")
	
	# Digita a mensagem no campo de postagem pelo atributo
	caixa_mensagem.send_keys(u"Teste de um script em Selenium incrível para postar em grupos do Facebook!\nBy Nicolas Pastorello")

	# Adiciona uma imagem
	if com_imagem:
		
		add_imagem = driver.find_element_by_name("view_photo").click()

		driver.find_element_by_name("file1").send_keys(caminho_imagem)
		driver.find_element_by_name("add_photo_done").click()
	
	# Espera a pagina ser carregada se a internet estiver lenta
	espera = driver.set_page_load_timeout(60 * 5)
	
	# Encontrar elemento do campo de publicar pelo atributo
	publicar = driver.find_element_by_name("view_post").click()

	# Encontrar elemento do campo de concluir pelo atributo
	finaliza = driver.find_element_by_name("done").click()

	# Espera 5 segundos
	time.sleep(5)

# Fechar navegador
driver.quit()
