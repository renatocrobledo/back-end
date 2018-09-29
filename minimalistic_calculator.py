'''
  Hoy fabricaremos una calculadora minimalista... 
  Las únicas operaciones que se se tendrán disponibles serán suma y resta
  
  Empezara pidiendo un número seguido del signo ( "+" ó "-" ) y después el segundo, 
  finalizando con el resultado de la operación correspondiente.. 
  esto se mantendrá en un ciclo hasta que se ingrese la palabra "salir":

  ejemplo:
  > 6
  > +
  > 2
  > 8
  > -
  > 7
  > 1
  > +
  > 23
  > 24
  > ... and so on until "salir" as input is detected
'''

result = 0
try:
  while True:
    value1 = input('valor1 ') if result == 0 else result

    if value1 == 'salir':
      break
    value1 = int(value1)

    sign = input('signo ') # should be + or -
    if sign == 'salir':
      break

    value2 = input('valor2 ')
    if value2 == 'salir':
      break
    value2 = int(value2)

    if sign == '+':
      result = value1 + value2
    elif sign == '-':
      result = value1 - value2
    else:
      raise ValueError('error al insertar el signo!, bye')
    print(result)
except ValueError as error:
  print('ups!', error)










