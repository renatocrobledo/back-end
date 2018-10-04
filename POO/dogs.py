
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

dogs_desription = [ {
                      'size': '30 cm',
                      'name': 'Firulais',
                      'color': 'white',
                      'breed': 'Schnutzer',
                      'weight': '3 kg'
                    },{
                      'size': '15 cm',
                      'name': 'Ñoño',
                      'color': 'gray',
                      'breed': 'Schnutzer',
                      'weight': '10 kg'
                    },{
                      'size': '5 cm',
                      'name': 'Arnulfo',
                      'color': 'white',
                      'breed': 'Chihuahua',
                      'weight': '300 gr'
                    },{
                      'size': '28 cm',
                      'name': 'Tronchatoro',
                      'color': 'green',
                      'breed': 'Chaw Chaw',
                      'weight': '15 kg'
                      }]
my_dog_list = []

for description in dogs_desription:
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