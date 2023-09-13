#Dados os Lados A,B,C de um triângulo, elaborar um programa para calcular
#e exibir os ângulhos internos desse triângulo (A,B,C)
import math as m    
A=float(input('Valor o valor do Lado A do triangulo: '))
B=float(input('Valor o valor do Lado B do triangulo: '))
C=float(input('Valor o valor do Lado C do triangulo: '))
AnguloA=m.acos((m.pow(B,2)+(m.pow(C,2))-(m.pow(A,2)))/(2*B*C))*180/m.pi
AnguloB=m.acos((m.pow(A,2)+(m.pow(C,2))-(m.pow(B,2)))/(2*A*C))*180/m.pi
AnguloC=m.acos((m.pow(A,2)+(m.pow(B,2))-(m.pow(C,2)))/(2*A*B))*180/m.pi
print('Os angulos internos são: A: ', AnguloA,'°','B: ',AnguloB,'°','C : ',AnguloC ,'°')
