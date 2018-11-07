
class We():
  @property
  def testing(self):
    print('eeaa!')
    d = {
      'w': self,
      'a': 1,
      'b': 2,
      'c': 3
    }

    return d

w = We()

w.testing
