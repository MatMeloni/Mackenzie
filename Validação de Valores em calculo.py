#Exemplo 3#
import math as m

n=int(input('Valor de n: '))
while n>0:
    print('valor nao suportado')
    n=int(input('Valor de n: '))
i=1
while i<=n:
    print('\n Cilindro',i)

    h=float(input('valor da altura: '))
    while h>0:
        print('valor nao suportado')
        h=float(input('valor da altura: '))

    R=float(input('valor do Raio maior: '))
    while R>0:
        print('valor nao suportado')
        R=float(input('valor da Raio maior: '))

    r=float(input('valor do Raio menor: '))
    while r<=0 or r>R:
        print('valor nao suportado')
        r=float(input('valor do Raio menor: '))

    v=m.pi*h*(m.pow(R,2)-m.pow(r,2))
    sl=2*m.pi*h*(R+r)
    print('\n O valor do volume vale: ',v)
    print('\n O valor da area lateral vale: ',sl)
    print('os valores do volume e da area são %2f e %2f' %(v,sl))