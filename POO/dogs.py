from dogs_description import dogs_list
from dog_class import Dog

my_dog_list = []

for description in dogs_list:
    new_dog = Dog(**description)
    my_dog_list.append(new_dog)

print("================================")

for dog in my_dog_list:
  print(dog.my_weight())

'''
first_dog = Dog(**dog_desription)
first_dog.bark()
first_dog.eat()
'''