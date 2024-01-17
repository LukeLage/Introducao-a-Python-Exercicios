#Construa um programa que receba um número inteiro positivo informado pelo usuário. 
#Caso ele seja par, o programa deve calcular o seu quadrado. 
#Mas, se ele for ímpar, deve ser calculado o seu cubo. 
#Ao fim, o programa deve imprimir o valor calculado. 


num = int(input('Digite seu número '))

if num % 2 == 0: 
    quadrado = num ** 2
    print ('Seu número é par e o quadrado de seu número é: ', + quadrado)
else:
    cubo = num ** 3
    print ('Seu número é ímpar e o cubo de seu número é: ', + cubo)
