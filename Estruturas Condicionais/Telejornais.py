#Em sua programação semanal, uma rede de televisão apresenta os seguintes telejornais:
#• Bom Dia Nação, apresentado por Zé PINHEIRO e Ana Carla ARAÚJO
#• Jornal Brasileiro, apresentado por Bill BONNER E CARLA VASCONCELOS
#Crie um programa no qual o usuário informe o sobrenome de um dos apresentadores. 
#Se o sobrenome informado não estiver na lista acima, o programa deve mostrar a mensagem “Apresentador(a) desconhecido(a).”. 
#Em caso positivo, o programa deve mostrar o nome do telejornal apresentado pelo apresentador(a).


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
