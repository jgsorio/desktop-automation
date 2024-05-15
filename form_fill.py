import pyautogui
import time

pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://docs.google.com/forms/d/e/1FAIpQLSdtYvVlFzsJVyACmFrGU_8hJMiMnQu_44-bSE9ClY2wHbhKDQ/viewform")
pyautogui.press("enter")

time.sleep(5)

pyautogui.press("tab", presses=3, interval=0.1)
pyautogui.typewrite("Ana Paula Duarte", interval=0.1)

pyautogui.press("tab")
pyautogui.typewrite('American Pie', interval=0.1)

pyautogui.press("tab")
pyautogui.press('enter')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(2)
pyautogui.press("tab")

pyautogui.press("space")
pyautogui.press('right', interval=0.3)
pyautogui.press('right', interval=0.3)
pyautogui.press('right', interval=0.3)
pyautogui.press('right', interval=0.3)
pyautogui.press('enter')


pyautogui.press('tab', interval=0.1)
pyautogui.press('tab', interval=0.1)
pyautogui.press('tab', interval=0.1)
pyautogui.press('enter')

pyautogui.alert('Finalizado com sucesso!', 'Fim!')
