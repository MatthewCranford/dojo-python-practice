my_dictionary = {
  "name": "Matt",
  "age": 26,
  "country": "US",
  "language": "Python"
}

def print_dict(dict):
  print dict["name"]
  print dict["age"]
  print dict["country"]
  print dict["language"]


for key in my_dictionary:
  print "Key=" + str(key) 
  print "Value=" + str(my_dictionary[key])
