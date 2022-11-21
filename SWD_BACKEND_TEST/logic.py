person = {}

person['fname'] = 'Joe'
person['lname'] = 'FoneBone'
person['age'] = 51
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = [
    {
        'type': 'dog',
        'name': 'Tuu',
        'detail':{
            'race': 'bull dog',
            'age': 10,
            'color': 'white'
        }
    },
    {
        'type': 'cat',
        'name': 'Meow',
        'detail':{
            'race': 'siamese cat',
            'age': 5,
            'color': ['black', 'white']
        }
    }
]

#print(person['pets'][1]['detail']['color'][1])

cat_color=[]

for color in person['pets'][1]['detail']['color']:
    cat_color.append(color)
    if 'black' in cat_color:
        break

print(cat_color)


