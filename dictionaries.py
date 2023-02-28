"""
Dictionaries

contents: key/value pairings
mutable: can be changed
order: maintain order of entry as of python 3.7
syntax: curly braces contain keys and values
keys and values separated by a colon

years = {"layla":1974, "ackeem": 1997}
"""
stuff = {"food": 15, "energy": 60, "enemies": 3}

# returns the value of the item in the dictionaire
print(stuff.get("food"))

# return the values of the dictionaire in ordem and dont need to pass the param
print(stuff.items())

# return the keys of the items
print(stuff.keys())

# return the values of the items
print(stuff.values())

# allow us to remove the last value in the dictionaire
print(stuff.popitem())

# allow us to see  what value is of a key in the dictionaire
print(stuff.setdefault("energy"))
print(stuff)

# allows us to set the key/value default when a key is not in the dictionary and to add that value to the dictionary.
print(stuff.setdefault("bodyBalance", 35))
print(stuff)

# the update method allows us to update the first dictionary with another dictionary.
new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

# We can update existing items in the dictionary through the same process.
new_items = {"rocks": 8, "arrows": 20}
stuff.update(new_items)
print(stuff)

# we can update and add new items at the same time with the update method.
up_items = {"rocks": 12, "webs": 20}
stuff.update(up_items)
print(stuff)
