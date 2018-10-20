try:
  number = int(input('Give me the number '))
  print('Par' if number % 2 == 0 else 'Impar')
except Exception:
  print('Ups... no entiendo que show!')