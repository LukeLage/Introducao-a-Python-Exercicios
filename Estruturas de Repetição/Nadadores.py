#Os professores de Educação Física estão organizando uma seletiva para montar a equipe de natação. 
#Para isso, eles convocaram os 7 melhores tempos da última competição e marcaram o tempo de cada um dos nadadores, na prova dos 25 metros, estilo livre.
#Considerando que não houve tempos iguais, construa um programa que leia o nome e o tempo (em segundos) de cada atleta e, em seguida, gere o seguinte relatório:
#a. nome do nadador com o melhor tempo
#b. nome do nadador com o pior desempenho
#c. tempo médio dos nadadores e
#d. quantidade de atletas com o tempo entre 12s e 15s


nadadores = []

for i in range(7):
    nome = input('Qual o nome do nadador {}? \n' .format(i+1))
    tempo = int(input('Qual o tempo em segundos do nadador {}? \n' .format(i+1)))
    nadadores.append((nome, tempo))

maior_tempo = max(nadadores)
print('O nadador com maior tempo e seu tempo em segundos foi: {}' .format(maior_tempo))

menor_tempo = min(nadadores)
print('O nadador com o menor tempo e seu tempo em segundos foi: {}' .format(menor_tempo))

media_tempo = sum([tempo for nome, tempo in nadadores]) / len(nadadores)
print('A média de tempo entre todos os nadadores é de: {:.2f}' .format(media_tempo))

atleta_media = len([nome for nome, tempo in nadadores if 12 <= tempo <= 15])
print ('A quantidade de atletas que teve seu tempo entre 12s e 15 foi de: {}' .format(atleta_media))
