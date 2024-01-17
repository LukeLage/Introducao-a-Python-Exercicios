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