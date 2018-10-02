def print_values(dictionary = {}):
  for key in dictionary:
    print(key, dictionary[key])


my_first_dictionary = {
  'name': 'Panfilo',
  'last_name': 'Membrillo',
  'age': '99',
  'phone': 123456789,
  'books': ['Math', 'Arts'],
  'address': {
    'street': 'menjurje',
    'number': 999
  }
}

print_values(my_first_dictionary)

# =========================================

myList1 = ['Sofía', 'Carlos', 'Mauricio', 'Rafa', 'Fabian', 'Beatriz', 'Pablo', 'Edgar', 'Santiago']
myList2 = ['pepe', 'lepu']


size = len(myList)
print(myList)
myList.sort(reverse=True,key=len)
print(sorted(myList))
print(myList.pop(0))
my_new_list = [*myList1, *myList2]
print(my_new_list)
numbers = [2, 1, 3, 1000, 100, 5, 4]
print(sorted(numbers))


