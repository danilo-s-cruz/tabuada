'''
GERADOR DE TABUADA DE MULTIPLICAÇÃO
'''
while True:
    print('-' * 40)
    print('TABUADA DE MULTIPLICAÇÃO')
    print('-' * 40)

    try:
       numero = int(input('Digite um número inteiro para gerar a Tabuada: '))
    except ValueError:
        print('O valor digitado não é um número inteiro. Tente novamente!')
        continue
    
    print(f'Tabuada de {numero}:')
    for n in range(1, 11):
        print(f'{numero} x {n} = {numero * n}')

    opcao = input('Digite qualquer tecla para continuar ou S para sair: ').strip().upper()
    if opcao == 'S':
        print('Saindo... Até a próxima!!')
        break