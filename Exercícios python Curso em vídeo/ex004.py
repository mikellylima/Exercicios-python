a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaço? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfafbético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É maiúsculo? ', a.isupper())
print('É minúsculo? ', a.islower())
print('Está capilalizado? ', a.istitle()) #Letra inicial maiúscula