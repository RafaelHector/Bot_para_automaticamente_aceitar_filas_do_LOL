from pyautogui import * 
import pyautogui #biblioteca utilizada para fazer a leitura
from time import sleep #tempo antes da ativação de uma função
import smtplib, ssl
from email.mime.multipart import MIMEMultipart #biblioteca para o envio de email
from email.mime.text import MIMEText


def click(x, y): #função responsável por clicar no botão de aceitar partida, x e y são a posição do botão
    pyautogui.moveTo(x, y) #parâmetros de onde ela vai clicar
    pyautogui.click()

def send_email(receiver_email): #enviara um e-mail informando que a partida foi encontrada
    if len(receiver_email) == 0:
        return

    # Constantes que será preenchida por você
    SENDER_EMAIL = "email@gmail.com" 
    PASSWORD = "senha123" 
    MESSAGE = "Sua fila no league of legends foi aceita!"

    #envio de email, de, para, destinatário
    msg = MIMEMultipart()
         
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = "LOL - Partida Encontrada"
     
    # adicionar o corpo da mensagem
    msg.attach(MIMEText(MESSAGE, 'plain'))
 
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()  #pode ser omitida
            server.starttls(context=context)
            server.ehlo()  #pode ser omitida
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
    except:
        print('Não foi possível enviar email de notificaçao para "' + receiver_email + '"')

def check_screen(): #será responsável por analisar a tela do pc e reconhecer quando uma partida for encontrada
    button_pos = pyautogui.locateOnScreen('fila.png', confidence=0.7) #função pyautogui que localizará na tela do PC se há uma imagem semelhante a importada no programa.
    #é importante a imagem ser bem semelhante à animação do momento de se aceitar uma partida na fila, já que o pyautogui a usará como referência. (a minha possuí o "Ativar o Windows", e não, não írei atualizar).
    #confidence=0.7, seria a semelhança da imagem, necessária ser ao menos 70% igual.
    #dica: tire um print do seu cliente, e utilizando o paint, recorte a parte que será a referência.
            
    if button_pos != None: #aqui ele encontrará a imagem, !=, não é ìgual a none
        #print(f'Found {button_pos}')
        click(button_pos.left, button_pos.top)
        return True
    
    return False

def main(): #a partir daqui as funções terão um início
    receiver_email = input('Seu email (opcional): ').strip()
    queue_counter = 0

    print('Estou de olho na fila...', end="\n\n")
    
    while True: #enquanto for verdade
        if check_screen(): #checando a tela
            queue_counter += 1
            print(f'Filas aceitas: {queue_counter}')
            
            send_email(receiver_email)         
            sleep(6)
            #break


main()        