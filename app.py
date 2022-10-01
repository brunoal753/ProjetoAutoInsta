import webbrowser
import pyautogui
from time import sleep


# abrir o site webbrowser.open('https://instagram.com')
webbrowser.open('https://instagram.com')
# colocar um usuário e senha ( já está automaticamente )
# clicar em "log in"
sleep(4)
tecla_entrar = pyautogui.locateCenterOnScreen('entraa.png')
pyautogui.click(tecla_entrar[0],tecla_entrar[1],duration=2)
pyautogui.click()
sleep(6)
# clicar em pesquisar
tecla_pesquisar = pyautogui.locateCenterOnScreen('pesquisarCinza.png')
pyautogui.click(tecla_pesquisar[0],tecla_pesquisar[1],duration=2.5)
# procurar uma pag (ex: nike)
pyautogui.typewrite('Nike')
# entrar na pag
sleep(4)
tecla_nike = pyautogui.locateCenterOnScreen('nike.png')
pyautogui.click(tecla_nike[0],tecla_nike[1],duration=1)
# clicar na ultima post
sleep(3)
#tecla_mosaico = pyautogui.locateCenterOnScreen('acimaPubli.png')
#pyautogui.click(tecla_mosaico[0],tecla_mosaico[1],duration=2)
pyautogui.moveTo(810,648,duration=2)
pyautogui.click()
# verificar se já curtiu aquela postagem ou não
sleep(3)
tecla_coracao = pyautogui.locateCenterOnScreen('coracaoCurtir.png')
pyautogui.click(tecla_coracao[0],tecla_coracao[1],duration=1.5)
sleep(1)
tecla_comentar = pyautogui.locateCenterOnScreen('balaoComentar.png')
pyautogui.click(tecla_comentar[0],tecla_comentar[1],duration=1.5)
pyautogui.scroll(-300)
sleep(2)
tecla_coment = pyautogui.locateCenterOnScreen('coment.png')
pyautogui.click(tecla_coment[0],tecla_coment[1],duration=1.5)
# Rolar para a caixa de comentar
sleep(1)
# Clicar na carinha de seleção de emoji
caixaDeEmoji = pyautogui.locateCenterOnScreen('carinhaemoji.png')
pyautogui.click(caixaDeEmoji[0],caixaDeEmoji[1],duration=1)
sleep(6.5)
# Colocar um emoji no comentário de 100
caixa_comentar_emoji = pyautogui.locateCenterOnScreen('100.png')
pyautogui.click(caixa_comentar_emoji[0],caixa_comentar_emoji[1],duration=2)
# Comentar
sleep(3)
pyautogui.typewrite('Niceee!')
# Publicar comentário
caixa_publi = pyautogui.locateCenterOnScreen('publicar.png')
pyautogui.click(caixa_publi[0],caixa_publi[1],duration=2)


# Clicar fora da publi
pyautogui.moveTo(1260,271,duration=1.5)
pyautogui.click()

sleep(2)
tecla_pesquisar = pyautogui.locateCenterOnScreen('pesquisarCinza.png')
pyautogui.click(tecla_pesquisar[0],tecla_pesquisar[1],duration=3)
# procurar uma pag (ex: cris)
pyautogui.typewrite('cristiano')
# entrar na pag
sleep(2)
tecla_cris = pyautogui.locateCenterOnScreen('cristiano.png')
pyautogui.click(tecla_cris[0],tecla_cris[1],duration=1.5)
# clicar na ultima post
sleep(2)
#pyautogui.moveTo(810,648,duration=1.5)
pyautogui.moveTo(819,488,duration=1.5)
pyautogui.click()
# verificar se já curtiu aquela postagem ou não
sleep(3)
tecla_coracao = pyautogui.locateCenterOnScreen('coracaoCurtir.png')
pyautogui.click(tecla_coracao[0],tecla_coracao[1],duration=1.5)
sleep(3)
tecla_comentar = pyautogui.locateCenterOnScreen('balaoComentar.png')
pyautogui.click(tecla_comentar[0],tecla_comentar[1],duration=1.5)
sleep(3)
# Rolar para a caixa de comentar
# Clicar na carinha de seleção de emoji
caixaDeEmoji = pyautogui.locateCenterOnScreen('carinhaemoji.png')
pyautogui.click(caixaDeEmoji[0],caixaDeEmoji[1],duration=2)
sleep(3.5)
# Colocar um emoji no comentário de 100
caixa_comentar_emoji = pyautogui.locateCenterOnScreen('emoji100.png')
pyautogui.click(caixa_comentar_emoji[0],caixa_comentar_emoji[1],duration=2)
pyautogui.click()
# Comentar
sleep(2)
pyautogui.typewrite('BORA CRISSS! BORA FI DO CRISS!!')
# Publicar comentário
caixa_publi = pyautogui.locateCenterOnScreen('publicar.png')
pyautogui.click(caixa_publi[0],caixa_publi[1],duration=2)
# Mais emoji
caixa_comentar_emoji = pyautogui.locateCenterOnScreen('emoji100.png')
pyautogui.click(caixa_comentar_emoji[0],caixa_comentar_emoji[1],duration=2)
pyautogui.click()
pyautogui.alert(text='ACABOU')
