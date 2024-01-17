jornais = ['Bom dia, Nação', 'Jornal Brasileiro']

apresentadores = ['Zé Pinheiro', 'Ana Carla Araújo', 'Bill Bonner', 'Carla Vasconcelos']

for apresentador in apresentadores:
    print(apresentador)


sobrenome = input('Qual o sobrenome do apresentador que você deseja assistir?\n')
sobrenome = sobrenome.upper()

if sobrenome == 'PINHEIRO' or sobrenome == 'ARAÚJO': 
    print ('Você deseja ver: "Bom Dia, Nação"')
elif sobrenome == 'BONNER' or sobrenome == 'VASCONCELOS':
    print ('Você deseja ver "Jornal Brasileiro"')
else: 
    print('Apresentador(a) desconhecido(a)')