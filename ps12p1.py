#input
name=input("Please Enter your full name:")

l=name.split()# using split function of string

#process,output
for word in l:
  word=word.strip
if len(l)==1:
  print("You have given only firstname , please complete your name")
else:
  print("the name in the form last name, first initial, such as (Lastname, F): ")
  print("{} {}".format(l[1],l[0][0]))
