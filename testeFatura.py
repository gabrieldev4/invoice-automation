def sendBill(self,f):
    try:
        # Definindo pausa
        pyautogui.PAUSE=2

        # Ajustando tamanho da tela para 80%
        pyautogui.hotkey('ctrl', '-')
        pyautogui.hotkey('ctrl', '-')

        # Coordenada da primeira fatura
        faturaX = 29
        faturaY= 404
        # Coordenada do wpp
        wppX = 1220
        wppY = 410

        # Diferença de tamanho entre as faturas
        difF = 40

        # Diferença ate wpp
        difW = 39
        # Faça enquanto i < f(totalLoops)
        i=1
        while(i<f):
            j=1
            while(j<5): # Envie 5 faturas
                # Selecionar fatura
                pyautogui.click(faturaX, faturaY)

                # Clicar no whatsapp
                pyautogui.click(wppX, wwpY)
            
                # Esperar tela carregar
                pyautogui.sleep(30)
                # Pressionar enter
                #pyautogui.press('enter')
                # Fechar wpp
                pyautogui.hotkey('ctrl','w')
                # Voltar para a página

                # Calculo para selecionar próx fatura
                faturaY+= difF
                wppY+= difW
                
                # iterador
                j +=1    
            # Iterador
            for l in range (5):
                pyautogui.click(x=1315, y=656)
            i+=1
        
        # Confirmação de sucesso da função
        print("Faturas enviadas")
    except:
        # Erro na função
        print("Erro, função não iniciada")

chrome = sendBill(totalLoops)

