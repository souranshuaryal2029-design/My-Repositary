
key = {}


key = {2: 'apple', 2: 'ball'}


key = {'name': 'bob', 2: [3, 6, 8]}

key = {'name': 'bob', 'age': 100}


print(key['name'])
print(key.get('age'))


key['age'] = 100
print(key)


key['address'] = 'uphill'
print(key)


key.pop('age')
print(key)


print("Address : ", key.get('address'))


key.clear()
print(key)