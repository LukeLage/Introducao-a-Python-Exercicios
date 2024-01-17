idades = []

while True: 
    idade = int(input('Informe a idade de um aluno (informe uma idade negativa para encerrar) \n'))
    if idade < 0: 
        break
    idades.append(idade)
    
maior = max(idades)
print ('A maior idade entre os alunos é: {}' .format(maior))

menor = min(idades)
print('A menor idade entre os alunos é de {}' .format(menor))

media = sum(idades) / len(idades)
print ('A média de idade entre os alunos é de: {:.2}' .format(media))