import math 
co = float(input('Digite o comprimento do cateco oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(ca, co)
print('O comprimento da hipotenusa é {}'.format(h))