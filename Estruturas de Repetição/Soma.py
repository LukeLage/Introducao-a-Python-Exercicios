#Crie um programa no qual o usuário informe 2 números inteiros: a e b. 
#Para que o programa continue sua execução, verifique se a < b. 
#Se sim, calcule a soma dos números inteiros no intervalo [a, b]. 
#Caso contrário, informe uma mensagem de erro.


a = int(input('Digite o primeiro número inteiro: \n'))
b = int(input('Digite o segundo número inteiro: \n'))

if a < b: 
    soma = sum(range(a, b+1))
    print ('A soma dos números entre A e B é: {}' .format(soma))
else: 
    print('Erro!')
