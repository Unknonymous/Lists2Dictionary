name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
#lists above were copied from the learning platfom per the assignment requirements

def Dmake(list1, list2):                    #sets the function
    tionary = {}                            #initializes tionary as a new dictionary
    for i in range (0,  len(list2)):        #loops through the list(s)
        tionary[list1[i]] = list2[i]        #sets the keys and values of tionary
    print tionary                           #prints the new dictionary, "tionary"
        
Dmake(name, favorite_animal)                #calls the user defined function

#The same can be accomplisched with the built-in functions zip() and dict(), shown below

def Dmake2(list1, list2):                   #this function makes use of the built-in functions zip(), and dict() to accomplish the same task as above
    for i in range (0, len(list1)):
        new = zip(list1, list2)
        newDict = dict(new)
    print newDict

#Dmake2(name, favorite_animal)              #commented out the calling of Dmake2 to prevent duplicate output during instructor testing