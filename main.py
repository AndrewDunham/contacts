from pathlib import Path

def main():
	#Take name input, save to file as name, 
	nameL = input("Welcome, please input your last name: ")
	nameF = input("Thank you, please input your first name: ")

	fileName = nameL + nameF + ".txt" #Creating filename that is the last and first name combinded together
	filePath = "./people/" + fileName
	myFile = Path("./people/", fileName)
	read = True

	if myFile.is_file():
		updateView = input("Your file exists, would you like to update or view information? (u/v): ")
		if(updateView == "u"):
			print("Function update will run")
			'''f = open(filename, "a")
			for i in range(2):
				f.write("Appended line %d\r\n" % (i+1))
			f.close()'''
			read = False
		else:
			openFile = open(filePath, "r")

			print("What would you like to view?")
			print(" 1. Name\n 2. Birthdate\n 3. Number\n 4. Social Media")
			viewInput = int(input("Please input the number of the topic you would like to view: "))
			for value in openFile:
				info = openFile.readlines(viewInput + 1)
				print(info)
				openFile.close()

	else:
		create = input("Your file does not exist, would you like to create a new file? (y/n): ")
		if (create == "y"):
			file = open(filePath, "w+")
			print("Created new file with name ")

	#Else create file
	#Save to file, nameLast = nameL, nameFirst = nameF
	#Each line of the file would corospond to a specific value, eg. line 1 is last name, line 2 is first name etc. 
	#Alternative would possibly be to use a database for more secure storage of files, but for this time this works.



if __name__ == "__main__":
	main()
