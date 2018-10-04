class Robot:
  def __init__(self, message = 'Hello'):
    self.message = message
  def say_hello(self, text = ''):
    print(self.message, text)

class Robot_v2(Robot):
  def walk(self):
    print('I can walk!!!!')

my_first_robot = Robot('Hi')
my_second_robot = Robot('Holaaa')
my_third_robot = Robot_v2('Que show')

my_first_robot.say_hello()
my_second_robot.say_hello()
my_third_robot.say_hello('Everybody! I\'m version two')

my_third_robot.walk()


