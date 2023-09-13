#Dados um Raio(R) de uma esfera e a altura (H) de uma calota esférica, elaborar um programa C++ para calcular e exibir a Área (A),
#o VOlume(V) e o raio (R) da base da calota esférica
import math as m
R=float(input('Informe o valor do raio da calota esférica: '))
H=float(input('Informe o valor da altura da calota esférica: '))
A=2*m.pi*R*H
r=m.sqrt(2*R*H-m.pow(H,2))
V=1/3*m.pi*H*(3*m.pow(r,2)+m.pow(H,2))
V2=1/6*m.pi*H*(3*m.pow(R,2)+m.pow(H,2))
print('O valor da Area da calota esférica é: ',A)
print('O valor do Volume é: ',V)
print('O valor do raio menor é: ',r)



