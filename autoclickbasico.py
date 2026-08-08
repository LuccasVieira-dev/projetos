#começo de um autoclicker simples em python, por enquanto fiz apenas o estrutural, devo atualizar futuramente
#esse foi um dos códigos mais limpo que eu ja fiz então se quiser utilizar por já deve funcionar corretamente


import tkinter as tk
import time
import keyboard
import threading
import pydirectinput



###JANELA TKINTER###

janela = tk.Tk()
janela.geometry("500x400")
janela.resizable(False, False)
janela.title("Simple Autoclicker by rato")
janela.eval('tk::PlaceWindow . center')
janela.protocol("WM_DELETE_WINDOW", janela.destroy)

def definir_velocidade():
    global velocidade
    velocidade = float(entrada.get())

entrada = tk.Entry(janela, font=("Arial", 14))
entrada.place(x=150, y=100, width=200, height=30)

botao = tk.Button(janela, text="Aplicar", command=definir_velocidade, font=("Arial", 12))
botao.place(x=200, y=140, width=100, height=35)

vel_texto = tk.Label(janela, text="coloque aqui a velocidade do autoclicker:", font=("Arial", 12))
vel_texto.place(x=100, y=70)

###AUTOCLICKER###

velocidade = 0.001

ativo = threading.Event()


print("F7 = ligar")
print("F8 = desligar")


def ligar():
    ativo.set()
    print("ligado")


def desligar():
    ativo.clear()
    print("desligado")


def clicking():
    while True:
        ativo.wait()
        pydirectinput.click()
        time.sleep(velocidade)


keyboard.add_hotkey("f7", ligar)
keyboard.add_hotkey("f8", desligar)


thread_click = threading.Thread(target=clicking, daemon=True)
thread_click.start()


janela.mainloop()