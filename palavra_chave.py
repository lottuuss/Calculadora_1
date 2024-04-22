#jogo que exibe a palavra chave


palavra_secreta= 'ratoeira'
letras_acertadas= ''
tentativas = 0
while True:
    
    letra_digitada = input('digite uma letra:')
    tentativas += 1
    if len(letra_digitada) > 1:
        print('digite apenas uma letra')    
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
         
    if palavra_formada == palavra_secreta:
       
        print('parabens voce ganhou')
        print('a palavra era', palavra_secreta)
        print('tentativas', tentativas)
        letras_acertadas= ''
        tentativas = 0