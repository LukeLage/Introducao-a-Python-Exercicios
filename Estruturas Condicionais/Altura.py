#Crie um programa que solicite ao usuário a informação de 3 estaturas. 
#Caso existam estaturas iguais, o programa deve apresentar a mensagem “Há, pelo menos, 2 pessoas com a mesma estatura”. 
#Caso contrário, o programa deve informar a maior estatura.


altura1 = int(input('Digite a altura da primeira pessoa em cm: \n'))
altura2 = int(input('Digite a altura da segunda pessoa em cm: \n'))
altura3 = int(input('Digite a altura da terceira pessoa em cm: \n'))

if altura1 == altura2 or altura2 == altura3 or altura1 == altura3:
    print ('Há pelo ou menos duas alturas iguais')
else: 
    if altura1 > altura2 or altura1 > altura3: 
        print('A primeira pessoa é a maior')
    elif altura2 > altura3 or altura2 > altura1:
        print('A segunda pessoa é a maior')
    elif altura3 > altura1 or altura3 > altura2:
        print('A terceira pessoa é a maior')
