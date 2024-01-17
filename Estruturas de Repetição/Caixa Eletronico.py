# Imagine um sistema de caixa eletrônico. Construa um programa que receba a senha de um correntista para validar o seu acesso ao sistema. 
#Considere que a senha fictícia do correntista é 123456. 
#Considere as seguintes restrições:
#• quando a senha estiver correta, mostrar a mensagem: “Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!"
#• quando o usuário errar a senha pela primeira vez,mostrar a mensagem: “Senha incorreta! Você aindatem 2 tentativas.”
#• se o usuário errar a senha pela segunda vez, mostrar a mensagem: “Senha incorreta! Você ainda tem 1 tentativa.”
#• se o usuário errar a senha novamente, mostrar a mensagem “Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.” e o programa deve ser encerrado.


tentativas = 3
senha_conta = 123456

cliente = input('Digite seu nome completo: \n')

while tentativas > 0: 
    senha = int(input('Digite a senha de seis dígitos da conta: \n'))
    if senha == senha_conta:
        print('Bem vindo, senhor(a) {}' .format(cliente))
        break
    else:
            tentativas -= 1
            if tentativas > 0:
                print('Senha incorreta! Você ainda tem {} tentativas' .format(tentativas))
            else:
                print('Sua senha foi bloqueada, por favor, dirija-se até um de nossos caixas')
