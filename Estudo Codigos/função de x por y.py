import math as m

x=float(input('Qual o Valor de X:'))
if x!=5:
    y=(m.pow(2*x,2)-3)/(x-5)
    print('o valor de y é de:',y)
if  x==5:
    print('nao tem função')