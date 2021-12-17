import re
import string

# Method for listing frequency of items
def frequencyOfItem(int = ""):
#Opens and reads file
   filename = "input.txt"
   f = open(filename, "r")
#Error message if file not found
   if not f:
       print("Error. File not found")
   else:
       data = f.read()
       listOfItems = data.split()  # Splits items
       frequency = {}   #Dictionary for frequency
       for item in listOfItems:
           frequency[item] = frequency.get(item,0)+1  #Counts # of times item in list

       returnString = ""
#Function to print list
       for item, freq in frequency.items():
           returnString += item + ":" + str(freq) + '\n'
           print(returnString)
       return 0
#Method for finding specific item
def frequencySpecificItem(itemName):
#Opens and reads file
    filename = "input.txt"
    f = open(filename, "r")
#Error message if file not found
    if not f:
        print("Error. File not found")
#When file is found and read:
    else:
        data = f.read()
        listOfItems = data.split() #Split entries into items
        frequency = {}
        #Counts items
        for item in listOfItems:
            frequency[item] = frequency.get(item,0)+1
        #Returns number of times item appears in file
        if itemName in frequency:
            print(itemName+": " + str(frequency[itemName]) +" purchased")
            return 0
        #Input validation
        else:
            print("Item not found.")
            return -1
        

#Method for creating histogram
def histogram(string=""):
    filename = "input.txt"
    f = open(filename, "r")
    if not f:
        print("Error, File not found")
    else:
        data = f.read()
        listOfItems = data.split()
        frequency = {}
        for item in listOfItems:
            frequency[item] = frequency.get(item,0)+1
        
#Prints * for each time item appears in file
        for item, freq in frequency.items():
            print(item +" -  "+ "*"*freq + '\n')
            
        return 0