
import random

def toss(number):
  heads = 0
  tails = 0
  
  for i in range(1, number + 1):
    coin = random.randint(0,1)
    if coin == 0:
      heads += 1
      print "Attempt #" + str(i) + ": " +"Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"  
    if coin == 1:
      tails += 1
      print "Attempt #" + str(i) + ": " +"Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    if i == 200:
      print "Ending the program, thank you!"  

toss(200)