#CRIAR O JOGO DA FORCA
import time
import os

bankWord = ["bola","casa","dragao","dinossauros","victor","lavandeiria","computador","escola","python","mesa","escrivaninha","segunda","terça","sexta"]

import random

tabuleiro=[

    '''
    +-----------+
    |           |
                |
                |
                |
                |
                |
                |
                |
    ==============
    ''',
    '''
    +-----------+
    |           |
    O           |
                |
                |
                |
                |
                |
                |
    ==============
    ''',
    '''
    +-----------+
    |           |
    O           |
    |           |
    |           |
                |
                |
                |
                |
    ============== 
    ''',
    '''
    +-----------+
    |           |
    O           |
   /|           |
    |           |
                |
                |
                |
                |
    ==============  
    ''',
    '''
    +-----------+
    |           |
    O           |
   /|\          |
    |           |
                |
                |
                |
                |
    ==============   
    ''',
    '''
    +-----------+
    |           |
    O           |
   /|\          |
    |           |
   /            |
                |
                |
                |
    ==============    
    ''',
    '''
    +-----------+
    |           |
    O           |
   /|\          |
    |           |
   / \          |
                |
                |
                |
    ==============     
    
    '''
]

def game_over()->str:

    print('''
               _ _ _ _ _ _   _ _ _ _ _ _     _ _           _ _   _ _ _ _ _ _   _ _ _ _ _ _        _ _ _ _ _                            _ _ _ _ _ _       _ _ _ _ _ _         
              |          |  |           |   |   \         /   |  |             |          |      |          |  \                  /   |                 |           |                       
              |             |           |   |    \       /    |  |             |          |      |          |   \                /    |                 |           |
              |             |           |   |     \     /     |  |             |          |      |          |    \              /     |                 |           |
              |    _ _ _ _  | _ _ _ _ _ |   |      \_ _/      |  |_ _ _ _ _ _  |_ _ _ _ _ |      |          |     \            /      |_ _ _ _ _ _      |_ _ _ _ _ _|
              |          |  |           |   |                 |  |             |      \          |          |      \          /       |                 |      \ 
              |          |  |           |   |                 |  |             |       \         |          |       \        /        |                 |       \ 
              |          |  |           |   |                 |  |             |        \        |          |        \      /         |                 |        \ 
              |_ _ _ _ _ |  |           |   |                 |  |_ _ _ _ _ _  |         \       |_ _ _ _ _ |         \ _ _/          |_ _ _ _ _ _      |         \  
     
            '''
            )       
    

def chamar_palavra()-> str:
    a=random.choice(bankWord)
    return a

def mostra_quantidade(b):
    tam_palavra=[]
    b=len(b)
    for i in range(b):
    #print("A palavra é ", "_ " *b)
        tam_palavra.append("_")
    print (tam_palavra)



def digitar_palavra()->str:
    c=input("Digite uma letra ").lower()
    return c

def main_game():
        palavra = chamar_palavra()
        mostra_quantidade(palavra)
        print(tabuleiro[0])

        tentativa=0
        i=0
        f=0

        confere=list(palavra)
        tam_confere=len(confere)
        for i in range (tam_confere):
            confere[i]="_"


        while tentativa!=6:
            teste= digitar_palavra()
            if palavra.count(teste)!=0 :#and not confere.count(teste):
                tam=len(palavra)
                for i in range(tam):
                    if teste in palavra[i] and confere[i]=="_" and not confere==palavra:
                        confere[i]=teste
                        tentativa=tentativa
                    
                
                
                if confere==list(palavra):
                    print("Você ganhou -. A palavra é ", palavra)
                    tentativa=6
                    break        
                print(" A palavra por enquanto é",confere)
                
                
            
            
            else:
                
                    print("Não acertou - tente novamente")
                    tentativa+=1
                    f+=1
                    os.system('cls')
            
                    print(confere)
                    print(tabuleiro[f])

        if confere==list(palavra:list):
        #print("Voce Acertou")
            tentativa=6
        else:
            os.system('cls')
            print("A palavra correta é ", palavra)
            game_over()   
            
        


def chamada():

    os.system('cls')
    enquanto=0

    while enquanto!='s':
        main_game()
        print(''' Digite qualquer tecla para continuar -
                  Digite a tecla "S" para Sair do Game   
            ''')
        enquanto=(input()).lower()
        os.system('cls')

chamada() 