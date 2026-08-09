#começo de um autoclicker simples em python, por enquanto fiz apenas o estrutural, espere atualizações futuras
#esse foi um dos códigos mais limpos que eu ja fiz então se quiser utilizar por já, deve funcionar corretamente


import tkinter as tk
import time
import keyboard
import threading
import pydirectinput


###VARIÁVEIS/CONFIGS###

velocidade = 0.1
ativo = threading.Event()
pydirectinput.PAUSE = 0

###TKINTER###

janela = tk.Tk()
janela.geometry("500x400")
janela.resizable(False, False)
janela.title("Simple Autoclicker by rato")
janela.eval('tk::PlaceWindow . center')
janela.protocol("WM_DELETE_WINDOW", janela.destroy)


def definir_velocidade():
    global velocidade

    if entrada_segundos.get() == "":
        entrada_segundos.insert(0, "0")
    if entrada_milissegundos.get() == "":
        entrada_milissegundos.insert(0, "0")

    segundos = float(entrada_segundos.get())
    milissegundos = float(entrada_milissegundos.get())
    velocidade = segundos + (milissegundos / 1000)
    marcador.config(text=f"Velocidade: {velocidade}s")

entrada_segundos = tk.Entry(janela, font=("Arial", 14))
entrada_segundos.place(x=125, y=160, width=100, height=30)
entrada_segundos.insert(0, "0")

entrada_milissegundos = tk.Entry(janela, font=("Arial", 14))
entrada_milissegundos.place(x=275, y=160, width=100, height=30)
entrada_milissegundos.insert(0, "100")

botao = tk.Button(janela, text="Aplicar", command=definir_velocidade, font=("Arial", 12))
botao.place(x=200, y=200, width=100, height=35)

vel_texto = tk.Label(janela, text="segundos:", font=("Arial", 12))
vel_texto.place(x=100, y=130)

vel_texto_ms = tk.Label(janela, text="milissegundos:", font=("Arial", 12))
vel_texto_ms.place(x=250, y=130)

marcador = tk.Label(janela, text=f"Velocidade: {velocidade}s", font=("Arial", 12))
marcador.place(x=100, y=240)

###AUTOCLICKER###

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
keyboard.add_hotkey("enter", definir_velocidade)

thread_click = threading.Thread(target=clicking, daemon=True)
thread_click.start()


janela.mainloop()