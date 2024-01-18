#Funções das fórmulas geométricas

def circulo():
    raio = float(input('Informe o raio do círculo: \n'))
    area_circulo = 3.14 * (raio * raio)
    
    print('A área do círculo é: {:.2f}' .format(area_circulo))

def triangulo():
    base = float(input('Informe a base do triângulo: \n'))
    altura = float(input('Informe a altura do triângulo: \n '))
    area_triangulo = (base * altura) / 2
    
    print('A área do triângulo é: {:.2f}' .format(area_triangulo))

def retangulo():
    base = float(input('Informe a base do retângulo: \n'))
    altura = float(input('Informe a altura do retângulo: \n'))
    area_retangulo = base * altura
    
    print('A área do retângulo é: {:.2f}' .format(area_retangulo))

#Funções para escolher a fórmula desejada

escolhas = ['Números de seleção das fórmulas:', '1 - Círculo', '2 - Triângulo', '3 - Retângulo']
print(escolhas)
selecao = {}

#Função para chamar as funções desejadas:

while selecao != 1 and selecao != 2 and selecao != 3:
    selecao = int(input('Informe o número da fórmula desejada: \n'))
    if selecao == 1: 
        circulo ()
        break
    elif selecao == 2:
        triangulo()
        break
    elif selecao == 3:
        retangulo()
        break
    else: 
        print('Fórmula inválida, por favor, selecione outra.')
