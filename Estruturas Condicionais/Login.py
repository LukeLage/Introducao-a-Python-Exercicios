#Suponha que o professor Fábio possui 2 logins na rede acadêmica da instituição. 
#Construa um programa que valide o acesso do professor à rede. 
#Caso o par usuário/senha informado esteja correto, o programa deve imprimir a mensagem “Seja bem vindo!”. 
#Caso contrário, “Usuário e senha não conferem”.
#login 1 usuário: procopio senha: 12345
#login 2 usuário: paiva senha: 54321


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
    
