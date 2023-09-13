import math
x=float(input('Valor de x:'))

if x<-1:
    y=math.pow(x,2)+1
    print('O valor de y é de:',y)
    if x==-1:
        y=0
        print('O valor de y é de:',y)
        if x==1:
            y=0
            print('O valor de y é de:',y)
            if -1<x<1:
                print('nao tem função')
                if x>1:
                    y=math.pow(x,2)+1
                    print('O valor de y é:',y)