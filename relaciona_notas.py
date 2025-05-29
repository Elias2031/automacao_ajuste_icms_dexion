import pandas as pd
import pyautogui
import time
# openpyxl

tempo_para_aguardar = 1

def clicar_e_aguardar(x,y):
    pyautogui.click(x,y)
    time.sleep(tempo_para_aguardar)

def escrever_e_aguardar(texto):
    pyautogui.write(texto)
    time.sleep(tempo_para_aguardar)

def pressionar_enter_e_aguardar():
    pyautogui.press('enter')
    time.sleep(tempo_para_aguardar)

def double_click_e_aguardar(x,y):
    pyautogui.doubleClick(x,y)
    time.sleep(tempo_para_aguardar)

def pressionar_e_aguardar(tecla):
    pyautogui.press(tecla)
    time.sleep(tempo_para_aguardar)

def verifica_participante():
    try:
        img = pyautogui.locateCenterOnScreen('participante_nao_cadastrado.png', confidence=0.5)
        return img is not None
    except pyautogui.ImageNotFoundException:
        # Lida com a exceção informando que a imagem não foi encontrada
        print('Imagem não encontrada na tela')
        return False


empresa = input('Por favor digitar o numero da empresa :')

mes = input('Por favor digitar o mês que vai ser alterado da seguinte forma xx/xxxx :')

nome_excel = input('Por favor digitar o nome do excel, optar por nomes juntos ou separados por hifens e traços :')

excel = pd.read_excel(nome_excel)

pyautogui.alert('O programa sera executado agora')

clicar_e_aguardar(12, 209)

escrever_e_aguardar(mes)

pressionar_enter_e_aguardar()

escrever_e_aguardar(empresa)

pressionar_enter_e_aguardar()

double_click_e_aguardar(440, 485)

clicar_e_aguardar(904, 173)

clicar_e_aguardar(807, 423)

escrever_e_aguardar('a')

pressionar_enter_e_aguardar()

clicar_e_aguardar(803, 423)

clicar_e_aguardar(753, 492)

escrever_e_aguardar('i')

for index, linha in excel.iterrows():

    if pd.isna(linha).all():
        pyautogui.alert('Alterações concluidas com sucesso')
        break

    pressionar_e_aguardar('down')

    pressionar_enter_e_aguardar()

    pressionar_e_aguardar('up')

    pressionar_enter_e_aguardar()

    escrever_e_aguardar('00')

    pressionar_enter_e_aguardar()

    if pd.isna(linha['PARTICIPANTE']):
        escrever_e_aguardar('1')
    else:
        escrever_e_aguardar(str(int(linha['PARTICIPANTE'])))

    pressionar_enter_e_aguardar()

    if verifica_participante():
        novo_participante = '0' + str(int(linha['PARTICIPANTE']))
        pressionar_enter_e_aguardar()
        escrever_e_aguardar(novo_participante)
        pressionar_enter_e_aguardar()

    if verifica_participante():
        novo_participante = '00' + str(int(linha['PARTICIPANTE']))
        pressionar_enter_e_aguardar()
        escrever_e_aguardar(novo_participante)
        pressionar_enter_e_aguardar()

    if verifica_participante():
        escrever_e_aguardar('1')
        pressionar_enter_e_aguardar()

    escrever_e_aguardar(str(int(linha['MODELO'])))

    pressionar_enter_e_aguardar()

    escrever_e_aguardar(str(int(linha['SERIE'])))

    pressionar_enter_e_aguardar()

    pressionar_enter_e_aguardar()

    escrever_e_aguardar(str(int(linha['NF'])))

    pressionar_enter_e_aguardar()

    escrever_e_aguardar(str(linha['EMISSAO']).replace('/',''))

    pressionar_enter_e_aguardar()

    escrever_e_aguardar(str(linha['VALOR']))

    pressionar_enter_e_aguardar()
    
    pressionar_enter_e_aguardar()

    escrever_e_aguardar(str(linha['ICMS']))

    pressionar_enter_e_aguardar()
    pressionar_enter_e_aguardar()
    pressionar_enter_e_aguardar()
    pressionar_enter_e_aguardar()
