#Dar play e esperar 5 segundos 
#Ele pega o conteudo do txt



import pyautogui, time
time.sleep(5)
texto = open('texto.txt', encoding='utf8')
for frase in texto:
    pyautogui.typewrite(frase)
    pyautogui.press('enter')




