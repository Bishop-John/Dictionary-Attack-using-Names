import csv

lowerCaseNames = []
upperCaseNames = []
titleCaseNames = []

guesses = 1

with open ("First Names.csv") as namesFile:
    reader = csv.DictReader(namesFile)
    for row in reader:
        titleCaseNames.append(row['NAME'])
        lowerCaseNames.append(row['NAME'].lower())
        upperCaseNames.append(row['NAME'].upper())


password = input("Set your password using any English name... ")

for i in range(len(lowerCaseNames)):
    #print ("Checking - ", lowerCaseNames[i])
    if lowerCaseNames[i] == password:
        print ("Solved - Password was", lowerCaseNames[i])
        print ("Guesses =", guesses)
        break
    else:
        guesses = guesses + 1
        
for i in range(len(upperCaseNames)):
    #print ("Checking - ", upperCaseNames[i])
    if upperCaseNames[i] == password:
        print ("Solved - Password was", upperCaseNames[i])
        print ("Guesses =", guesses)
        break
    else:
        guesses = guesses + 1

for i in range(len(titleCaseNames)):
    #print ("Checking - ", titleCaseNames[i])
    if titleCaseNames[i] == password:
        print ("Solved - Password was", titleCaseNames[i])
        print ("Guesses =", guesses)
        break
    else:
        guesses = guesses + 1
