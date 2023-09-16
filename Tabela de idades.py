print('Idade - Bronze(Opçao 1) -Ouro (Opçao 2)\n'
'até 18 anos - R$500,00 - R$650,00\n'
'18 a 49 anos - R$750,00 - R$925,00\n'
'50 a 64 anos - R$950,00 - R$1300,00\n'
'65 a 79 anos - R$1300,00 - R$ 1800\n'
'80 anos ou mais - R$2000,00 - R$2600,00\n')

idade=int(input('Informe a idade do usuario: '))
while idade<1 or idade>120:
  print('Idade Invalida')
  idade=int(input('Informe a idade do usuario: '))
op=int(input('Informe a opçao desejada: \n'))
while op<1 or op>2:
  print('Opçao Invalida')
  op=int(input('Informe a opçao desejada: \n'))


if idade<18:
  if op==1:
    print('Valor: R$500,00')
  if op==2:
    print('Valor: R$650,00')
          
elif idade>=18 and idade<=49:
  if op==1:
    print('Valor: R$750,00')
  if op==2:
    print('Valor: R$925,00')
    
elif idade>=50 and idade<=64: 
  if op==1:
    print('Valor: R$950,00')
  if op==2:
    print('Valor: R$1300,00')
    
elif idade>=65 and idade<=79:
  if op==1:
    print('Valor: R$1300,00')
  if op==2:
    print('Valor: R$1800,00')
    
else:
  if op==1:
    print('Valor: R$2000,00')
  if op==2:
    print('Valor: R$2600,00')