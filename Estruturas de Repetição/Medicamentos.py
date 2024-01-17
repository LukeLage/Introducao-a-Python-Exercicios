#Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o usuário formou cinco medicamentos distintos). 
#O programa deve informar o nome e o preço do medicamento mais barato, bem como a média aritmética dos preços informados.


quantidade = int(input('Quantos deseja inserir? \n'))

medicamentos = []

for i in range(quantidade):
    nome = input("Insira o nome do medicamento {}: \n".format(i + 1))
    preco = float(input("Insira o valor do medicamento {}: \n".format(i + 1)))
    medicamentos.append((nome, preco))

menor = min(medicamentos)
print('O medicamento de menor valor é: {}' . format(menor))

media = sum([preco for nome, preco in medicamentos]) / len (medicamentos)
print ('A média de preço entre os os {} medicamentos é de: R${:.2f}' .format(quantidade, media))
