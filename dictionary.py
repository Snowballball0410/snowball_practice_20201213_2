MLB_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')])
Snowball = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

print(type(MLB_team))
print(MLB_team)
print(len(MLB_team))

# Dictionary elements are not accessed by numerical index ex.MLB_team[1] is wrong
print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])

# Adding an entry to an existing dictionary
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)

MLB_team['Seattle'] = 'Seahawks'
print(MLB_team)

# delete an entry
del MLB_team['Seattle']
print(MLB_team)

# an object of any immutable type can be used as a dictionary key
print(Snowball[0])
print(Snowball[2])
print(type(Snowball))

person = {}
print(type(person))
person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['fname'])
print(person['age'])
print(person['children'])
print(person['children'][-1])
print(person['pets']['cat'])

foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
print(foo)
print(foo[42])
print(foo[2.78])
print(foo[True])

foo.clear()
print(foo)

# d.get(<key>) searches dictionary d for <key> and returns the associated value if it is found
Snowball_dict = {'a': 10, 'b': 20, 'c': 30}
print(Snowball_dict.get('b'))
print(Snowball_dict.get('z'))
print(Snowball_dict.get('z', -1))

print(list(Snowball_dict.items()))
print(list(Snowball_dict.items())[1][0])
print(list(Snowball_dict.items())[1][1])

print(list(Snowball_dict.keys()))
print(list(Snowball_dict.values()))

Snowball_dict.pop('b')
print(Snowball_dict)
Snowball_dict.pop('z', -1)
print(Snowball_dict)

Snowball_dict.popitem()
print(Snowball_dict)

# two dictionaries merged together
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1)
