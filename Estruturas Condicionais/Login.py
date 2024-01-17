usuario1 = 'procopio'
senha1 = '12345'

usuario2 = 'paiva'
senha2 = '54321'

usuario = input('Usuário \n')
senha = input('Senha: \n')

if usuario == usuario1 and senha == senha1:
    print('Seja bem vindo!')
elif usuario == usuario2 and senha == senha2:
    print('Seja bem vindo')
else: 
    print ('Usuário e senha não conferem')
    