tipos_pagamento = ['Formas de Pagamento: ', '1 - À Vista', '2 - Cartão de Débito', '3 - Cartão de Crédito (Vencimento)']

for pagamento in tipos_pagamento:
    print(pagamento)
    
codigo = int(input('Digite o número que representa a forma de pagamento do cliente: \n'))
preco = float(input('Digite o valor da compra: \n'))

if codigo == 1: 
    desconto = preco * 0.15
    valor = preco - desconto
    print('O total à pagar é de: R$' + str(valor))
elif codigo == 2: 
    desconto = preco * 0.1
    valor = preco - desconto
    print ('O total à pagar é de: R$' + str(valor))
elif codigo == 3: 
    desconto = preco * 0.05
    valor = preco - desconto
    print ('O total à pagar é de: R$' + str(valor))
else:
    print('Essa forma de pagamento é inválida')