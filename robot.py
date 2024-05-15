# Robo que abre automaticamente o menu, procura o bloco de notas e escreve o texto que voce escolher
import pyautogui
import time

text = input("Escreva algo: ")

pyautogui.press("win")

pyautogui.typewrite("notepad", interval=0.1)
pyautogui.press("enter")

time.sleep(2)

pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace")

time.sleep(2)

pyautogui.typewrite(text, interval=0.1)
pyautogui.alert("terminou")
