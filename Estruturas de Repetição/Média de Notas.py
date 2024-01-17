#Uma turma da disciplina de Banco de Dados possui 5 alunos. 
#Construa um programa que leia duas notas e calcule a média aritmética de cada aluno. 
#Ao fim, de acordo com a tabela abaixo, indique o percentual de alunos em Prova Final.
#FAIXA RESULTADO
#média < 2 Reprovado
#2 ≤ média < 6 Prova Final
#média ≥ 6 Aprovado


medias = []

for i in range (5):
    nota1 = float(input('Insira a nota da primeira prova do aluno {} \n' .format(i+1)))
    nota2 = float(input('Insira a nota da segunda prova do aluno {} \n' .format(i+1)))
    media = (nota1 + nota2) / 2 
    
    medias.append(media)
    
prova = len([media for media in medias if 2 <= media <= 6])
percentual = (prova / 5) * 100

print('O percentual de alunos que estão na prova final é de {:.2f}% e a quantidade é: {}' .format(percentual, prova))
