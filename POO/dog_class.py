
class Dog:
  def __init__(self, name, breed, color, size, weight):
    self.name = name
    self.breed = breed
    self.color = color
    self.size = size
    self.weight = weight
    print(f"Hello, I'm {name} and I'm alive and my size is {size}!")
    
  def __str__(self):
    return self.name

  def bark(self, sound = "Wwwhoof!"):
   # print(self.name + " says: "  + sound)
    print(f"{self.name} says: {sound}")

  def eat(self, type_of_food = 'meat'):
    print(f"{self.name} is eating {type_of_food}, and its weight is {self.weight}")

  def my_weight(self):
    return f"I'm {self.name} and my weight is: {self.weight}"