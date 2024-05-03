# Importando bibliotecas
import pyautogui
import time
import re
import cv2
import pytesseract
import numpy as np

# Classe Navegador
class Navegador:
    def __init__(self):
        self.browser= "chrome"
        self.link = "https://www.sponteweb.com.br/"

    
    #  Entrar no sponte
    def openSistem(self):
        try:
            # Definindo pausa
            pyautogui.PAUSE=3
            # Abrir o windows
            pyautogui.press("win")
            # Digitar o chrome
            pyautogui.write(self.browser)
            # Apertar o enter
            pyautogui.press("enter")
            # Selecionar o meu perfil
            # for i in range(1,5):
            pyautogui.press("tab")
            pyautogui.press("enter")

            # Criar nova aba
            pyautogui.hotkey("ctrl","n")
            # Entrar no site
            pyautogui.write(self.link)
            pyautogui.press("enter")    

            # pyautogui.scroll(-200)

            #Se o código tiver dando erro ao carregar a página, usar o pyper pra copiar e colar
            # pyautogui.copy()

            time.sleep(3)
            pyautogui.press("enter")
            time.sleep(5)
            pyautogui.press("esc")
            pyautogui.press("F5")
            # clicar no financeiro
            pyautogui.click(x=328, y=150)
            # clicar no integração
            pyautogui.click(x=357, y=331)
            # clica nas faturas
            pyautogui.click(x=580, y=366)

            # Teste
            print("")
        except:
            print("Erro ao entrar no sistema")

    # Função captura
    def captureScreen(self,x,y, width, height):
        try:
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            return screenshot
        except:
            print("Erro ao capturar tela")
    
    def extract_number_from_image(self,image):
        # Salvar imagem temporariamente
        image.save("captured_screenshot.png")

        # Configurações do pytesseract
        custom_config = r'--oem 3 --psm 6 outputbase digits'

        try:
            # Usando pytesseract para extrair texto da imagem
            extracted_text = pytesseract.image_to_string("captured_screenshot.png", config=custom_config)
            
            # Usando expressão regular para extrair números
            numbers = re.findall(r'\d+', extracted_text)
            
            # Convertendo a lista de números em uma string
            extracted_number = ''.join(numbers)
            
            return extracted_number
        except Exception as e:
            print("Erro ao extrair número:", e)
            return None


    # Função calcular Loops
    def calcLoops(self, l):
            try:
                if l % 5 == 0:
                    totalLoops = int(l / 5)
                else:
                    totalLoops = int((l / 5) + 1)
                print(f"Total de loops calculados: {totalLoops}")
                return totalLoops
            except Exception as e:
                print(f"Erro ao calcular loops: {e}")
                return 0

    # Função enviar faturas
    def sendBill(self,f):
        try:
            # Definindo pausa
            pyautogui.PAUSE=2

            # Ajustando tamanho da tela para 80%
            pyautogui.hotkey('ctrl', '-')
            pyautogui.hotkey('ctrl', '-')

            
            # Faça enquanto i < f(totalLoops)
            i=1
            while(i<f):
                
                # Coordenada da primeira fatura
                faturaX = 30
                faturaY= 405
                # Coordenada do wpp
                wppX = 1220
                wppY = 410

                # Diferença de tamanho entre as faturas
                difF = 40

                # Diferença ate wpp
                difW = 39 
                # Envie 5 faturas  
                for _ in range(5):
                    # Selecionar fatura
                    pyautogui.click(faturaX, faturaY)

                    # Clicar no whatsapp
                    pyautogui.click(wppX, wppY)
                
                    # Esperar tela carregar
                    pyautogui.sleep(2)
                    # Pressionar enter
                    #pyautogui.press('enter')
                    # Fechar wpp
                    pyautogui.hotkey('ctrl','w')
                    # Voltar para a página

                    # Calculo para selecionar próx fatura
                    faturaY+= difF
                    wppY+= difW
                    
                # Iterador
                for l in range (5):
                    pyautogui.click(x=1336, y=602)
                i= i+1
            
            # Confirmação de sucesso da função
            print("Faturas enviadas")
        except:
            # Erro na função
            print("Erro, função não iniciada")


# Testes
# Entrar no sistemachrome

    
chrome = Navegador()
chrome.openSistem()

#Capturar imagem
captured_image = chrome.captureScreen(25,670,100,30)

#Extrair numero da imagem
captured_number = chrome.extract_number_from_image(captured_image)
print(captured_number)

#Calcular loops 
totalLoops = chrome.calcLoops(int(captured_number))

#Enviar faturas
send = chrome.sendBill(totalLoops)

