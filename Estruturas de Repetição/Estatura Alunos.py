quantidade = int(input('Quantos alunos há na escola? \n'))
estatura = []

for i in range(quantidade):
    tamanho = int(input('Adicione a estatura do aluno {} em cm: \n' .format(i+1)))
    estatura.append(tamanho)

menor = min(estatura)
print('A menor estatura da escola é de {} cm' .format(menor))

maior = max(estatura)
print('A maior estatura da escola é de {} cm' .format(maior))

media = sum(estatura)/quantidade
print('A estatura média da escola é de {:.0f} cm' .format(media))