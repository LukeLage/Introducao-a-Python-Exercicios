def dados_funcionarios():
    funcionarios = [
        {
            "Matricula": 1,
            "Nome": "Ana",
            "Sexo": "F",
            "Departamento": "TI",
            "Tempo de Serviço": 7,
            "Salário": 3200.00,
        },
        {
            "Matricula": 2,
            "Nome": "Beatriz",
            "Sexo": "F",
            "Departamento": "TI",
            "Tempo de Serviço": 4,
            "Salário": 3720.00,
        },
        {
            "Matricula": 3,
            "Nome": "Carla",
            "Sexo": "F",
            "Departamento": "TI",
            "Tempo de Serviço": 1,
            "Salário": 2100.00,
        },
        {
            "Matricula": 4,
            "Nome": "Daniela",
            "Sexo": "F",
            "Departamento": "RH",
            "Tempo de Serviço": 2,
            "Salário": 3920.00,
        },
        {
            "Matricula": 5,
            "Nome": "Emilio",
            "Sexo": "M",
            "Departamento": "RH",
            "Tempo de Serviço": 7,
            "Salário": 4235.12,
        },
        {
            "Matricula": 6,
            "Nome": "Fernando",
            "Sexo": "M",
            "Departamento": "Marketing",
            "Tempo de Serviço": 7,
            "Salário": 1200.00,
        },
        {
            "Matricula": 7,
            "Nome": "Gabriela",
            "Sexo": "F",
            "Departamento": "Marketing",
            "Tempo de Serviço": 8,
            "Salário": 7234.89,
        },
        {
            "Matricula": 8,
            "Nome": "Hernandez",
            "Sexo": "M",
            "Departamento": "TI",
            "Tempo de Serviço": 6,
            "Salário": 4234.12,
        },
        {
            "Matricula": 9,
            "Nome": "Ítalo",
            "Sexo": "M",
            "Departamento": "RH",
            "Tempo de Serviço": 13,
            "Salário": 13934.23,
        },
        {
            "Matricula": 10,
            "Nome": "Janaína",
            "Sexo": "F",
            "Departamento": "RH",
            "Tempo de Serviço": 7,
            "Salário": 9341.89,
        },
    ]
    return funcionarios

funcionarios = dados_funcionarios()

print("As mulheres no setor de TI que recebem mais de R$3000.00 são:")

for funcionario in funcionarios:
    if (
        funcionario["Sexo"] == "F"
        and funcionario["Departamento"] == "TI"
        and funcionario["Salário"] > 3000.00
    ):
        print([funcionario["Nome"]])

print('Os funcionarios com tempo de serviço maior que cinco anos são: ')

for funcionario in funcionarios: 
    if (
        funcionario['Tempo de Serviço'] > 5
    ):
        print(funcionario['Nome'])