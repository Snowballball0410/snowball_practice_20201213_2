import collections

de = collections.deque([1, 2, 3])
Snowball = collections.deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(de)

de.append(4)
print(de)

de.appendleft(6)
print(de)

de.pop()
print(de)

de.popleft()
print(de)

# using index() to print the first occurrence of 4
print(Snowball.index(4, 2, 5))

# using insert() to insert the value 3 at 5th position
Snowball.insert(4, 3)
print(Snowball)

# using count() to count the occurrences of 3
print(Snowball.count(3))

# using remove() to remove the first occurrence of 3
Snowball.remove(3)
print(Snowball)

# using extend() to add numbers to right end
# adds 4,5,6 to right end
Snowball.extend([4, 5, 6])
print(Snowball)

# using extendleft() to add numbers to left end
# adds 7,8,9 to right end
Snowball.extendleft([7, 8, 9])
print(Snowball)

# using rotate() to rotate the deque
# rotates by 3 to left
Snowball.rotate(-3)
print(Snowball)

Snowball.reverse()
print(Snowball)
