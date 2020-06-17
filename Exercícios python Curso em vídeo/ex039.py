from datetime import date
print('Programa para indicação de alistamento no serviço militar')
nascimento = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Digite seu sexo: ')).lower().strip()
ano_atual = date.today().year
idade = ano_atual - nascimento
if sexo == 'masculino':
    if idade < 18:
        print(f'Ainda precisa se alistar! Faltam {18 - idade} anos.')
        print(f'Seu alistamento será em {ano_atual + (18 - idade)}.')
    elif idade == 18:
        print('Você precisa se alistar este ano!')
    elif idade > 18:
        print(f'Você já deveria ter se alistado há {idade - 18} anos.')
        print(f'Seu alistamento foi em {ano_atual - (idade - 18)}.')
else:
    print('Seu alistamento não é obrigatório do serviço militar.')
