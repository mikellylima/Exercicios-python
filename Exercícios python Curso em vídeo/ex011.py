A = float(input('Digite a altura da parede: '))
L = float(input('Digite a largura da parede: '))
m = A * L
# 1L -> 2m^2
# ? -> m
print('Sua parede tem {}x{} e a área é de {:.2f}m².'.format(A, L, m))
print('Serão gastos {:.2f} litros para pintar a parede.'.format(m / 2))
