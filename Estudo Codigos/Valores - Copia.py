#Dado um valor de x qualquer, elaborar um programa em Python para verificar
#se o valor digitado é "positivo","nulo" ou "negativo".

x=float(input('qual o valor do x: '))

if x > 0:
    print('o valor do x é positivo')
elif x == 0:
    print('o valor de x é nulo')
else:
    print('o valor de x é negativo')

 