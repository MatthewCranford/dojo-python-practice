
a = [2,4,10,16]

def multiply(a,times):

  for i in range(0, len(a)):
    print a[i]
    a[i] = a[i] * times
  return a

print multiply(a,3)

