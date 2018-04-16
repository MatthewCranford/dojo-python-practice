
def odd_even(start,stop): 
  for i in range(start,stop+1):
    if (i % 2 == 0):
      print "Number is " + str(i) + ". This is an even number."
    else:
      print "Number is " + str(i) + ". This is an odd number."

odd_even(1,5)