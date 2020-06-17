from datetime import date
print('Programa para classificação de categorias através da idade')
nasc = int(input('Digite sua data de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria: mirim')
elif idade <= 14:
    print('Categoria: infantil')
elif idade <= 19:
    print('Categoria: juvenil')
elif idade <= 25:
    print('Categoria: sênior')
elif idade > 25:
    print('Categoria: master')
