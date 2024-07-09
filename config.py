
import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chr")
time.sleep(2)
pyautogui.click(x=540, y=613)
time.sleep(2)
pyautogui.click(x=687, y=59)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=581, y=411)   
pyautogui.hotkey("ctrl", "a")
pyautogui.write("emailvalidado@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.click(x=648, y=574)

time.sleep(3)

import pandas
tabela = pandas.read_csv("produtos.csv")
print (tabela)

for linha in tabela.index:

    pyautogui.click(x=573, y=292)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)