from calculadora import calculadora

calc = calculadora()

print('Hello, please enter with values.')
largura: float = float(input('Enter the width in meters: '))
profundidade: float = float(input('Enter the depth in meters: '))
altura: float = 2.9

# calc.area_paredes: float = 2*(largura+profundidade)*altura

print('The wall area is: ',
      calc.calcular_area_paredes(largura, altura, profundidade), 'm²')

print(
    'The ceiling area is',
    calc.calcular_area_teto(largura, profundidade), 'm²'
)

print(
    'The necessary quantity is :', calc.calculo_litragem_necessaria(), 'Liters'
)


