#O código abaixo é um exercício que tem como foco o recebimento de uma idade e retornar se
#a idade é correspondente à de uma criança, adolescente ou adulto
idade = int(input('Defina a idade do usuário:'))

if (idade >= 0) and (idade <= 12):
    print('O usuário é uma criança')

if (idade >= 13) and (idade <= 17):
    print('O usuário é um adolescente')
    
if idade >= 18:
    print('O usuário é um adulto')
    
if idade < 0:
    print('Rode o código novamente e digite uma idade válida:')