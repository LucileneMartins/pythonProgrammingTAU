"""
Collection of data
can contain any/all data types in a single list
can contain other collections (lists, dictionaries, tuples) as list items
mutable (tems can be added, removed, changed)
maintain order (can use index to find an item)

"""
# checking itens in the list

fruits = ["peaches", "grape", "pears", "apples", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print("apple" in fruits)  # false because there is not apple in the list
print("apples" in fruits)  # true because there is apples in the list
print(fruits.count("apples"))  # 3 because there are 3 apples in the list
print(fruits.index("apples"))  # returns the position of the item in the list
