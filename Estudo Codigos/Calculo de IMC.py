#Faça um programa que calcule e mostre o IMC (Índice de Massa Corporal) de uma pessoa, considerando
#que ela irá dizer qual o seu peso e qual a sua altura (IMC = peso/(altura*altura) ).
import math as m
Peso=float(input('Quanto você pesa: '))
Altura=float(input('Quanto você mede: '))
IMC=Peso/m.pow(Altura,2)
print('Seu IMC é de: ',IMC)
