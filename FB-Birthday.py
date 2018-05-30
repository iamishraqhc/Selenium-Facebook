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

# Acessa a página de aniversariantes do Facebook
driver.get("https://www.facebook.com/events/birthdays")

# Encontrar elemento do campo de mensagem pelo atributo
aniversariante = driver.find_elements_by_xpath('//*[@class="enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput"]')

# Para cada aniversariante manda os parabens
for parabens in aniversariante:
	parabens.send_keys(u"Parabéns Tudo de bom e do melhor na sua vida.")
	parabens.send_keys(Keys.RETURN)

	# Espera 2 segundos
	time.sleep(2)

# Fechar navegador
driver.quit()
