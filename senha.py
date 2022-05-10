
import getpass
import time
import os
from wsgiref.validate import validator

class chamada:

    def chama(self):
        print ( )
        print ( )
        print("E n t r e  c o m  s u a  s e n h a ----")
        print("Tem  que  ter  no  minimo  08  caractere")
        print("01 letra Maiuscula e  01 Letra Minuscula")
        print("Tem   quer  ter  pelos  um     número   ")
        print("01 caracter especial(! - @ - # - $ - % - &) ")
        a=getpass.getpass("Digite a sua senha: ")
        time.sleep(3)
        return a
#Funçao chamada está Ok.
    def tamanho(self, valor, verificacao):
        recebe=len(valor)
        verifica=verificacao
        if (recebe<8):
            verificacao=True
            return 0, verifica
        else:
            verifica=False
            return b, verifica
 #Função tamanho está ok.
   
    def caracatere_especial(self, valor,verificacao):
        valor=valor
        estado=verificacao
        
        if '$'  in valor:
            #print ("valor ok")
            estado=False
            return valor, estado
        elif '!' in valor:
            #print ("Valor Ok")
            estado=False
            return valor, estado
        elif '@' in valor:
            #print ("valor OK")
            estado=False
            return valor, estado
        elif '#' in valor:
            #print("valor ok")
            estado=False
            return valor, estado
        elif '%' in valor:
            #print("valor OK")
            estado=False
            return valor
        elif '&' in valor:
            #print("valor ok")
            estado=False
            return valor, estado
        else:
            #print("valor não Ok")
            estado=True
            return valor, estado
        estado=True
        return valor, estado
#Função caractere especial está ok
    
    def letra_maiuscula(self,valor, estado):
        valor=valor
        estado = estado
        tam=len(valor)       
        #tam=0
        vtam=0
        for i in valor:
                        
            if (i.isupper()==True):
                
                vtam=1
            else:
               
                tam=tam+1
        if (vtam==1):
            estado=False
            return valor, estado
        else:
            estado=True
            return valor, estado

    def numero(self,valor, estado):
        valor=valor
        estado = estado
        tam=len(valor)       
        #tam=0
        vtam=0
        for i in valor:
                        
            if (i.isnumeric()==True):
                
                vtam=1
            else:
               
                tam=tam+1
        if (vtam==1):
            estado=False
            return valor, estado
        else:
            estado=True
            return valor, estado

    def teste_final(self,valor, estado):
        print("Confirme a sua senha")
        d=getpass.getpass("Digite novamente")
        #print ("O valor é ",d)
        valor=valor
        if (d==valor):
             print("Sua senha foi cadastrada com sucesso")
             estado=False
             return valor, estado
        else:
             print("Cadastre novamente a senha")
             estado=True
             return valor, estado
         

inicio=True
a=chamada()                                     # chamada ok
while(inicio==True):                            
        b=a.chama()                             #função chamaok
        c=a.tamanho(b,False)                    #função tamanho ok
        d=a.caracatere_especial(b,False)        #função carcactere ok
        e=a.letra_maiuscula(b,False)
        f=a.numero(b,False)
        g=a.teste_final(b,False)
        inicio=(c[1])
        inicio=(d[1])
        inicio=(e[1])
        inicio=(f[1])
        inicio=(g[1])
   