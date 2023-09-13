a=float(input('informe o valor a: '))
b=float(input('informe o valor b: '))
c=float(input('informe o valor c: '))
if a<b:
    if a<c:
        menor=a
    else:
        menor=c
else:
    if b<c:
        menor=b
    else:
        menor=c
print('O menor valor é: ',menor)
