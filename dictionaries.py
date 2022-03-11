dict ={ 'name': ['a','b','c'],
        'age' : [24,45,76],
        'location' : ['agra', 'kanpur', 'delhi']}
for name, age,location in zip(dict['name'],dict['age'], dict['location']):
    print(f"My name is {name} and I'm {age} and i'm from {location}")
    
# -----------------------------------------------------------------------------

# merging dictionary
a = {'a': 1, 'b': 2}
b = {"c": 5, "d": 7}
z = {**a, **b}
print(z)
