#começo de um autoclicker avançado em python, por enquanto fiz apenas o estrutural, devo atualizar futuramente
#esse foi o código mais limpo que eu ja fiz então se quiser utilizar por já deve funcionar corretamente


import time
import keyboard
import threading
import pydirectinput

velocidade = 0.5

ativo = False

print("F7 = ligar")
print("F8 = desligar")


def ligar():
    global ativo
    ativo = True
    print("ligado")


def desligar():
    global ativo
    ativo = False
    print("desligado")


def clicking():
    while True:

        if ativo:
            pydirectinput.click()
            time.sleep(velocidade)
        else:
            time.sleep(0.01)


keyboard.add_hotkey("f7", ligar)
keyboard.add_hotkey("f8", desligar)

thread_click = threading.Thread(target=clicking)
thread_click.start()