
person = { "name":"Speros", "position":"Coding Dojo Overlord", "age":"young"}

def printer(person):
  for info in person:
    print info +"="+ person[info]

printer(person)