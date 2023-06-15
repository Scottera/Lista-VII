numero = int(input('Informe um número: '))

primo = True
for i in range(2, numero):
    if (numero % i ==0):
        primo = False
        break

if primo:
    print('O número é primo.')
else:
    print('O número não é primo.')
