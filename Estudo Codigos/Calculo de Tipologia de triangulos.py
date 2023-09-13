import math as m

a=float(input('valor de a:'))
b=float(input('valor de b:'))
c=float(input('valor de c:'))

if a>=b and a>=c:
    if a**a==b**b+c**c:
        print('retangulo')
    elif a**a>b**b+c**c:
        print('Obtusangulo')
    else:
        print('acutangulo')        
else:
    print('O lado A deve ser o maior')
