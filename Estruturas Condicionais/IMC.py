# O IMC (Índice de Massa Corporal) é utilizado para avaliar o peso de um indivíduo em relação à sua altura e, como resultado, indica se o indivíduo está com o peso ideal, acima ou abaixo do recomendado. 
#A tabela a seguir indica a situação de um indivíduo adulto em relação ao seu IMC:
#IMC Situação
#Abaixo de 18,5 Abaixo do peso
#Acima de 18,5 e menor que 25 Peso normal
#A partir de 25 e menor que 30 Sobrepeso
#Acima de 30 e menor que 35 Obesidade grau 1
#Acima de 35 e menor que 40 Obesidade grau 2
#Acima de 40 Obesidade grau 3
#Para calcular o IMC, é usada a fórmula IMC = peso / (altura*altura). 
#Construa um programa no qual um usuário informe seu peso e sua altura.
#A aplicação deve indicar o IMC calculado e a situação do indivíduo.


peso = int(input('Digite seu peso arredondado: \n'))
altura = float(input('Digite sua altura em m: \n'))

altura2 = altura * altura
IMC = peso / altura2 

if IMC < 18.5: 
    print('Você está abaixo do peso e seu IMC é: ' + str(IMC))
elif IMC > 18.5 and IMC < 25: 
    print ('Você está no peso normal e seu IMC é: ' + str(IMC))
elif IMC > 25 and IMC < 30: 
    print ('Você está acima do peso e seu IMC é: ' + str(IMC))
elif IMC > 30 and IMC < 35: 
    print ('Você está em obesidade grau 1 e seu IMC é: ' + str(IMC))
elif IMC > 35 and IMC < 40:
    print ('Você está em obesidade grau 2 e seu IMC é: ' + str(IMC))
elif IMC > 40:
    print ('Você está em obesidade grau 3 e seu IMC é: ' + str(IMC))
else: 
    print('IMC inválido')
