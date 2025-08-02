# 3. Check that a tuple type cannot be changed in python.

tuple = (23,"Harry")

# Tuples are immutable
tuple = tuple.append(19)

print(tuple)