"""
Collection of data
can contain any/all data types in a single list
can contain other collections (lists, dictionaries, tuples) as list items
mutable (tems can be added, removed, changed)
maintain order (can use index to find an item)

"""
fruits = ["apple", "strawberry", "grape", "lime"]
numbers = [1.5, 2.5, 3.5]

print(fruits)
print(numbers)

fruits.append("orange")
numbers.extend(fruits)

print(fruits)
print(numbers)

# removes the item in the list
fruits.remove("orange")
print(fruits)


# removes the first item in the list
fruits.pop(0)
print(fruits)


# removes the last item in the list
fruits.pop(-1)
print(fruits)

# sort - it can be useful when we need to sort a list, but will just work for items of like types
# In a numbers list, you can combine integers and floating-point numbers and they'll be sorted.

numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
numbers.sort()

print(numbers)
