#Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:
#Código Condição de Pagamento Desconto (%)
#1 À vista (em espécie) 15
#2 Cartão de débito 10
#3 Cartão de crédito (vencimento) 5
#Construa um programa que solicite ao operador do caixa o preço total da venda, bem como a forma de pagamento. 
#Ao fim, o programa deve informar o valor final a ser pago. 


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
