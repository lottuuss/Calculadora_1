
print('Digite uma frase'
'que vou extrair a letra que mais repetir')
frase = input('Digite a frase aqui: ')
i = 0
apareceu_mais_vezes = 0
quantas_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual== ' ':
        i +=1
        continue

    quantas_apareceu_1 = frase.count(letra_atual)
    
    if apareceu_mais_vezes <= quantas_apareceu_1:
       apareceu_mais_vezes = quantas_apareceu_1
       quantas_apareceu = letra_atual
    
    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'{quantas_apareceu} que apareceu '
    f'{apareceu_mais_vezes} x')