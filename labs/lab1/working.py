from arrays import LinearArray
x = LinearArray()
# Insert some items
x.insert(3)
x.insert(2)
x.insert(1)
# Look for an item; should return True
print(x.contains(2))
# Remove an item
x.remove(2)
# Look for an item; should return False
print(x.contains(2))