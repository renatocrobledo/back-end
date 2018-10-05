import dogs_description

class Dog:
  def __init__(self, name, breed, color, size, weight):
    self.name = name
    self.breed = breed
    self.color = color
    self.size = size
    self.weight = weight
    print(f"Hello, I'm {name} and I'm alive and my size is {size}!")

  def bark(self, sound = "Wwwhoof!"):
   # print(self.name + " says: "  + sound)
    print(f"{self.name} says: {sound}")

  def eat(self, type_of_food = 'meat'):
    print(f"{self.name} is eating {type_of_food}, and its weight is {self.weight}")

  def my_weight(self):
    return f"I'm {self.name} and my weight is: {self.weight}"

my_dog_list = []

for description in dogs_description.dogs_list:
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