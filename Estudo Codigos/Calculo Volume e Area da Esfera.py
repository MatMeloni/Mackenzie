import math as m

r=float(input('Informe o valor do raio da esfera: '))
alfa=float(input('Informe o valor do angulo: '))
V=2/3*m.pow(r,3)*alfa
A=2*m.pow(r,2)*alfa+m.pi*m.pow(r,2)
print('O valor do volume é: ',V)
print('O valor da area é: ',A)
