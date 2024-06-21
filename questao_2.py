nota1 = float(input('Digite a nota M1:'))
nota2 = float(input('Digite a nota M2:'))
nota3 = float(input('Digite a nota M3:'))

media = (nota1+nota2+nota3)/3

if (media >= 0) and (media <= 4):
    print('O aluno foi reprovado :(')
    
if (media >= 4.1) and (media <= 6.0):
    print('O aluno pôde fazer o exame final')
    final = float(input('Digite a nota do exame final:'))
    if (final > 6):
        print('O aluno foi aprovado! :)')
    else:
        print('O aluno foi reprovado :(')
            
if (media > 6):
    print('O aluno foi aprovado por média! :)')
    