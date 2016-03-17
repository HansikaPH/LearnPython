#Python dict(dictionary) for mapping/association

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2} #declaring a dictionary with curly braces

print stuff['name']
print stuff['age']
print stuff['height']

#adding new elements into the dictionary
stuff['city'] = "San Francisco"
print stuff['city']

#adding integer keys
stuff[1] = "Wow"
stuff[2] = "Neato"

print stuff[1]
print stuff[2]
print stuff

#deleting elements with the del keyword
del stuff['city']
del stuff[1]
del stuff[2]
print stuff

