my_dict = {'Макс' : 1995, 'Алексей' : 2015, 'Михаил' : 2005}
print(my_dict)
print(my_dict['Макс'])
my_dict.update({ 'Алена' : 1999,
                 'Жанна' : 2001})
print(my_dict)
del my_dict['Алексей']
print(my_dict.get('Алексей'))
print(my_dict)

my_set = {1, 2, 3, 'Name', True, 3, 2}
print(my_set)
my_set.update([34, 56, 'Age'])
print(my_set)
my_set.discard(1)
print(my_set)