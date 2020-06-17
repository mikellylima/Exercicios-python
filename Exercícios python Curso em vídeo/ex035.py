a = float(input('Digite o comprimento da reta 1: '))
b = float(input('Digite o comprimento da reta 2: '))
c = float(input('Digite o comprimento da reta 3: '))
if a < (b + c) and b < (a + c) and c < (b + a):
    print('As retas podem format um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
