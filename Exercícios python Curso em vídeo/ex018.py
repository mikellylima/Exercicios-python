from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo em graus: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O seno do ângulo {}° é: {:.2f}'.format(a, sen))
print('O cosseno do ângulo {}° é: {:.2f}'.format(a, cos))
print('A tangente do ângulo {}° é: {:.2f}'.format(a, tan))