# sum list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for item in a:
  sum += item
print sum

# averagelist
average = sum / len(a)
print average

# nest loops
a = [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [31, 12, 50, 42, 5], [47, 7, 4, 2, 31, 40, 49]]

for arr in a:
  for num in arr:
    print num
