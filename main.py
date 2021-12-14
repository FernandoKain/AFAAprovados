# Bibliotecas a serem usadas
import pyautogui
import time

pyautogui.click(x=713, y=700)

# Solicita entrada do usuário em relação ao número de atividades entregues.
var = int(input("Insira o número de alunos que entregaram as atividades: "))


# Alterna abas antes de começar o código
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

pyautogui.press('f2')
pyautogui.press('a')
pyautogui.press('p')
pyautogui.press('r')
pyautogui.press('o')
pyautogui.press('v')
pyautogui.press('a')
pyautogui.press('d')
pyautogui.press('o')


# Interando entre os alunos e imputando a nota 10.
for i in range(var-1):
    # pyautogui.press('1')


    pyautogui.press('enter')
    pyautogui.press('a')


pyautogui.hotkey('ctrl', 'pagedown')
pyautogui.hotkey('ctrl', 'pagedown')

for i in range(10):
    pyautogui.press('up')

pyautogui.press('down')
pyautogui.press('down')

for i in range(10):
    pyautogui.press('left')

for i in range (7):
    pyautogui.press('right')

pyautogui.press('f2')

pyautogui.press('r')
pyautogui.press('e')
pyautogui.press('s')
pyautogui.press('u')
pyautogui.press('l')
pyautogui.press('t')
pyautogui.press('a')
pyautogui.press('d')
pyautogui.press('o')

pyautogui.press('enter')

pyautogui.press('f2')

pyautogui.press('=')
pyautogui.press('f')
pyautogui.press('i')
pyautogui.press('n')
pyautogui.press('a')
pyautogui.press('l')
pyautogui.press('!')
pyautogui.press('a')
pyautogui.press('c')
pyautogui.press('6')

pyautogui.press('enter')

for i in range(var-1):
    pyautogui.hotkey('ctrl', 'd')
    pyautogui.press('enter')


pyautogui.hotkey('ctrl', 'pageup')
pyautogui.hotkey('ctrl', 'pageup')