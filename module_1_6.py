my_dict = {'Alex' : 1985, 'Masha': 1991, 'Armen': 1987, 'Katya': 1995}
print('Dict:', my_dict)
print('Existing value:',my_dict['Masha'])
print('Not existing value:',my_dict.get('Misha'))
my_dict.update({'Kolya': 1979,
                'Polina': 1989})
a = my_dict.pop('Polina')
print('Deleted value:',(a))
print('Modified dictionary:',(my_dict))
my_set = {1,2,'string',1,2,3,'string',(356,648,999),3,2,5,(356,648,999)}
print('Set:',my_set)
my_set.update(['bitcoin',13,])
my_set.remove('string')
print('Modified set:',my_set)