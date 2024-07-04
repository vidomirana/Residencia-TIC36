n2 = int(input('Digite um número inteiro: '))

while n2 > 0:
    print('========')
    print(n2)
    if(n2%2 == 0):
        print('par')
    else:
        print('ímpar')
    n2 -= 1