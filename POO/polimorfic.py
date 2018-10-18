class Shark():
  def swim(self):
    print('I\'m a shark and I\'m swiming')

class GoldFish():
  def swim(self):
    print('I\'m a goldFish and I\'m floating!')

def this_fish_gonna_swimm(fish):
  fish.swim()

memo = Shark()
this_fish_gonna_swimm(memo)

memo = GoldFish()
this_fish_gonna_swimm(memo)
