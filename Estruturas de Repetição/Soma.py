a = int(input('Digite o primeiro número inteiro: \n'))
b = int(input('Digite o segundo número inteiro: \n'))

if a < b: 
    soma = sum(range(a, b+1))
    print ('A soma dos números entre A e B é: {}' .format(soma))
else: 
    print('Erro!')