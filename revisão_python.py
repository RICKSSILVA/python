#class algoritmo():


def chama_vetor():
    print ("Digite uma Sequencia de 10 nomes: ")
    a=0
    vetor=[]
    while (a<10):
        
        nome=input("Digite o nome número")
        vetor.append(nome)
        a+=1
        print ("o vetor original é", vetor)
        #for n in vetor:

    ordena_nome(vetor)
        #   print (n);
    return vetor
def ordena_nome(vetor):
    vetor_original=vetor
    #print ("O vetor é ", vetor_original)
    #vetor_trabalho1=[]
    a=0
    b=0
    c=1
    recebe=0
    while (a<9):
        b=0
        c=1

        #print ("o vetor é ", vetor_original)
        
        while (b<9):

            #print (b)
            #print (c)
            
            if (vetor_original[b]>vetor_original[c]):
                    recebe=vetor_original[b]
                    vetor_original[b]=vetor_original[c]
                    vetor_original[c]=recebe
                    b=b+1
                    c=c+1
            else:
            
                b+=1
                c+=1
        a+=1
        #print("o valor de b apos", b, ", ", "vetor é ", vetor_original[b])
        #print("o valor de c apos", c, ", " , " vetor é ", vetor_original[c])
    print(vetor_original)
    return vetor_original

def pesquisa_nome(teste):
    vetor_original=teste
    print("o vetor é ", vetor_original)
    print("Favor digitar um nome")
    a=str(input("Entre com um nome  : "))
    i=0
    c=len(vetor_original)
    print("O tamando de c é ", c)
    for i in range(c):
        #print(i)
        print(vetor_original[i])
        if (a==vetor_original[i]):

            print ("Nome encontrado, na posição")
        else:
            print ("nome não encotrado")

   






a=chama_vetor()
d=pesquisa_nome(a)
print(d)
#print (vetor_original)

        

