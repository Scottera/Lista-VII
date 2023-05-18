num = int(input('Informe um número: '))
for i in range(num):
    if i % 3 ==0 or i % 7 ==0:
        print('*')
    else:
        print(i)