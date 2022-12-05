#input
line = input("Enter line of comma-separated-values: ")

#process  phase 
line_items = line.split(",")

#output
for item in line_items:
  print(item.strip())