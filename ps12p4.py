
def repeatShift(line):
	
	Chare = int(input("Enter #. of characters to print in each lines: "))
	
	Line = int(input("Enter #. of lines to print: "))
	
	scrDirection = input("Enter scroll direction of Line: Right: r || Left: l -> ")

	shift = ""
	if scrDirection == "r":
		shift = ""
	elif scrDirection == "l":
		shift = " " * (Line - 1)
	counter = 0
  
	for i in range(Line):
		print(shift, end='')

		if scrDirection == "r":
			shift += " "
		elif scrDirection == "l":
			shift = shift[:-1]
		
		for j in range(Chare):
			print(line[counter], end='')
			counter = (counter + 1) % len(line)
      
		print()
    
if __name__ == '__main__':
	line = input("Enter the line of text: ")
  
	repeatShift(line)