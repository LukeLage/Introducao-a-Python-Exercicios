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