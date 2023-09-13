import math

a=float(input('qual o valor de a:'))
b=float(input('qual o valor de b:'))
x=float(input('qual o valor de x:'))
y=float(input('qual o valor de y:'))

elipse=(math.pow(x,2)/math.pow(a,2))+(math.pow(y,2)/math.pow(b,2))
if elipse==1:
    print('esta na linha da elipse')
elif elipse<1:
    print('Esta dentro da elipese')
else:
    print('Esta fora da elipse')





