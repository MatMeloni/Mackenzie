import math 

r=float(input("Qual o raio da esferas: "))
a=float(input("Qual o valor da dimensao A:"))
b=float(input("Qual o valor da dimensao B:"))
h=float(input("Qual o valor da dimensao H:"))
Am=2*math.pi*r*h
Ao=math.pi*(2*r*h+math.pow(a,2)+math.pow(b,2))
V=1/6*math.pi*h*(3*math.pow(a,2)+3*math.pow(b,2)+math.pow(h,2))
print("A Área Lateral Am é de:",Am)
print("A Área Exterior Ao é de :",Ao)
print("O Volume é de: ",V)