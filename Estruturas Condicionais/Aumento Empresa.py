#Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo:
#Cargo Aumento(%)
#Programador de Sistemas 30
#Analista de Sistemas 20
#Analista de Banco de Dados 15
#Crie um programa que solicite ao usuário o salário e o cargo de um determinado funcionário. 
#Na sequência, o programa deve calcular e imprimir o seu novo salário. 
#Caso o cargo informado não esteja na tabela, o programa deve imprimir “Cargo inválido”.


cargos_empresa = ['Cargos da Empresa: \n', '1 - Programador de Sistemas \n', '2 - Analista de Sistemas \n', '3 - Analista de Banco de dados']

for cargo in cargos_empresa:
    print(cargo)

cargo_funcionario = int(input('Digite o número do seu cargo: \n'))
salario = int(input('Digite o seu salário atual: \n'))

if cargo_funcionario == 1: 
    aumento = salario * 0.3
    novo_salario = salario + aumento
    print ('O seu novo salário é de: ' + str(novo_salario))
elif cargo_funcionario == 2: 
    aumento = salario * 0.2
    novo_salario = salario + aumento
    print ('O seu novo salário é de: ' + str(novo_salario))
elif cargo_funcionario == 3:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print('O seu novo salário é de: ' + str(novo_salario))
else: 
    print ('Cargo inválido')
