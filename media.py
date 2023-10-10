def obter_nota():
    while True:
        nota = float(input('Digite sua nota (entre 0 e 10): '))
        if 0 <= nota <= 10:
            return nota
        else:
            print('A nota deve estar entre 0 e 10. Tente novamente.')

nota1 = obter_nota()
nota2 = obter_nota()
nota3 = obter_nota()

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'Sua média é de {media:.1f}\nVocê está aprovado, parabéns.')
else:
    print(f'Sua média é de {media:.1f}\nVocê foi infelizmente reprovado.')