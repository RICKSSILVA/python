

import smtplib
import email.message
import getpass

def enviar_email(a,b,c,d):
    a=a
    titulo=b
    titulo2=c
    mensagem=d
    corpo_email=f'''
            <h1><center>{titulo2}</center></h1></p>
            <p>{mensagem}</p>

    
    
    '''

    msg=email.message.Message()
    msg['Subject']= f'{titulo}'
    msg['From']='rickssilva1974@gmail.com'
    msg['To']=f'{a}'
    password=chama_password()
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)    
    s=smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'],password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('\nEmail enviado\n')


def cadastrar_email():
       
    email=input("DIGITE O EMAIL A SER ENVIADO  :  \n")

    return email
    
    
def titulo():
    #a=email
    chamada=input("Digite o Titulo do Email:\n")
   
    #enviar_email(email,chamada)

#enviar_email()
    return chamada

def mensagem():
    c=input("Digite o titulo no corpo do email\n")
    d=input("Digite a mensagem que irá ser enviada\n")
    return c,d
    
def chama_password():
    d=getpass.getpass("Entre com a Sua senha do email :  ")
    return d


try:
    tentativa =True
    while (tentativa==True):


        print ("############################################################################")
        print ("#                                                                          #")
        print ("#               PROGRAMA ENVIO AUTOMATICO DE EMAILS VIA - PYTHON           #")
        print ("#                                                                          #")
        print ("############################################################################")
        print ("#                   ETAPAS DE ENVIO DE EMAIL                               #")
        print ("# 1. Cadastrar email - Destinatário                                        #")
        print ("#    1.1 Cadastrar Titulo                                                  #")
        print ("#    1.2 Escreve o assunto                                                 #")
        print ("#    1.3 Solicitando a senha do email                                      #")
        print ("#    1.4 Enviar   o email                                                  #")  
        print ("#  Para finalizar o programa digite N para Sair  ou S para Continuar       #")
        print ("############################################################################")
        

        a=cadastrar_email()
        b=titulo()
        c=mensagem()
        enviar_email(a,b,c[0],c[1])
        teste=input("Deseja enviar mais algum email - (S/N)\n")
        if (teste=='s' or teste=='S'):
            tentativa=True
        elif(teste=="n" or teste=="N"):
            tentativa=False
except:
    print("OPÇÃO ERRADA ")
