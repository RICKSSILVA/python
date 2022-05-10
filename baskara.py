import math

def passa_parametros():
    print("Informe o valor dos coeficientes: ")
    coeficiente_a = int(input("Coeficiente A: "))
    coeficiente_b = int(input("Coeficiente B: "))
    coeficiente_c = int(input("Coeficiente C: "))

    if(coeficiente_a>0):
        calcula_delta(coeficiente_a, coeficiente_b, coeficiente_c)
    else:
        print("Valor do coeficiente A é igual a zero, portanto não é uma equação de segundo grau.")

def calcula_delta(a, b, c):
    a=a
    b=b
    c=c
    print (a)
    print (b)
    print (c)
    #print('Valores A = {}, B = {}, C = {} '.format(a, b, c))
    delta = pow(b,2)-(4*a*c)
    print ("o valor de delta é", delta)

    calcula_raizes(delta, a, b, c)
    #calcula_raizes(a,b,c,delta)

def calcula_raizes(delta, a, b, c):

    #print('Valores A = {}, B = {}, C = {} e delta {} '.format(a, b, c, delta))
    print(delta)
    if(delta < 0):
        print("delta menor")
        print("O valor de delta é negativo, não existem raízes reais")

    elif(delta == 0):
        print ("delta igual")
        raiz = -b/(2.0*a)
        print()
        print("O valor de delta é igual a zero e possui somente uma raiz")
        print("O valor da raiz é {}".format(raiz))

    elif(delta > 0):

        delta=int(delta)
        print ("delta calcualo", delta)
        teste = math.sqrt(delta)
        
        raiz_x1 = (((-1*(b)) + (teste))) / (2 * a)

        raiz_x2 = (((-1*(b)) - (teste))) / (2 * a)

        print("O valor de delta é positivo e a equação possui duas raízes reais")
        print("O valor da primeira raiz é {} é o valor da segunda raiz é {}".format(raiz_x1, raiz_x2))



passa_parametros()
