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