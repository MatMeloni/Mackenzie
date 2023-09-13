# Projeto Formulas #

import math as m

forma=str(input("qual a forma do calculo:"))
print("a forma é:",forma)

mylist=["triangulo","quadrado","cubo","esfera","losangulo","prisma"]
if forma in mylist:
    print(forma)
else:
    print("não existe formula")

