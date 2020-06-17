from math import pow
print('Cálculo do IMC')
p = float(input('Digite seu peso(kg): '))
h = float(input('Digite sua altura(m): '))
imc = p/pow(h, 2)
print('O IMC é igual a {:.2f}.'.format(imc))
if imc < 18.5:
    print('Condição: abaixo do peso')
elif 18.5 <= imc < 25:
    print('Condição: peso ideal')
elif 25 <= imc < 30:
    print('Condição: sobrepeso')
elif 30 <= imc > 40:
    print('Condição: obesidade')
elif imc >= 40:
    print('Condição: obesidade mórbida')
