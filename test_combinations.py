from random import randint

max_nice_list_lenght = 3
combinations_found = 0
nice_list = []

def fits_equation(tupl, constant = 33):
  (s1,s2,s3,s4,c1,c2,c3,c4) = tupl
  return ((s1*c1)+(s2*c2)+(s3*c3)+(s4*c4)) == constant

print('Here I go....')
while True:
  # from 0 to 5
  while True:
    s1 = randint(0, 5)
    s2 = randint(0, 5)
    s3 = randint(0, 5)
    s4 = randint(0, 5)
    if  0 < (s1 + s2 + s3 + s4) <= 5:
      break
  # from 1 to 14
  c1 = randint(0, 14)
  c2 = randint(0, 14)
  c3 = randint(0, 14)
  c4 = randint(0, 14)

  if fits_equation((s1,s2,s3,s4,c1,c2,c3,c4)):
    nice_list.append((s1,s2,s3,s4,c1,c2,c3,c4))
    print('{} of {}'.format(combinations_found, max_nice_list_lenght))
    combinations_found += 1
    if len(nice_list) == max_nice_list_lenght:
      print(nice_list)
      break 

# algoritmo de simplex 


'''
s1,s2,s3,s4,c1,c2,c3,c4
(0, 1, 5, 1, 7, 12, 2, 11)
'''