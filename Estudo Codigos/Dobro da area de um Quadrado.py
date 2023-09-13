#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário (Area=Lado*Lado)
import math as m
Lado=float(input('Qual o valor do Lado do quadrado: '))
Area=m.pow(Lado,2)
print('O dobro da area do quadrado é:',Area*2)