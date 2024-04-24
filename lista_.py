#lista simples para aprender

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar meus itens: ')

    if opcao == 'i':
        os.system('cls')
        valor= input('inserir: ')
        lista.append(valor)
    elif opcao == 'a':
        os.system('cls')
        for i, valor in enumerate(lista):
            print(i,valor)
        indice_str =input('Escolha o item que deseja apagar: ')
        try:
            
            indice= int(indice_str)
            del lista[indice]
            os.system('cls')
       
        except ValueError:
            
            print('Por favor digite o numero de acordo com o item')  
        except IndexError:
            print('Este item não consta na lista')

    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Não há produtos na lista')

        for i, valor in enumerate(lista):
            print(i,valor)    
    
    else:
        print('Por favor escolha i,a ou l ')
        