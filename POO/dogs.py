from dogs_description import dogs_list
from dog_class import Dog

my_dog_list = []

def add_dog():
  print('==================')
  name = input('name ')
  size = input('size ')
  color = input('color ')
  breed = input('breed ')
  weight = input('weight ')
  
  new_dog = Dog(name, breed, color, size, weight)
  my_dog_list.append(new_dog)

def show():
  print(my_dog_list)

def menu():
    print('[i] introducir nuevo registro')
    print('[m] mostrar todos los perrunos')
    print('[s] salir')
  
while True:
  menu()
  option = input()
  if option == 's':
    print('Bye!')
    break
  elif option =='i':
    add_dog()
  elif option =='m':
    show()
