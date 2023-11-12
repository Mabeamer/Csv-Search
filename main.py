import csv
import sys
from csv import writer
import os
import pandas as pd

#cv search function

##TODO: CREATE AN OBJECT THAT HOLDS A LIST OF THESE VALUES TO REFERENCE THAT INSTEAD OF CONSISTENTLY REBUIDLING
reader = csv.reader(open('us-area-code-cities.csv', encoding="utf8"))



#display what line the user should search frm (area code example, city, state, long/lat)
#once selected have them search
#display all found references to file
#passing in placeholder***

def main():
    class fileSearch:
        def __init__(self, userData):
            self.userData = userData

    #placeholder name || allow the user to input a file and it will read from there
    userFile = fileSearch("")
    data = []
    #uh
    for row in reader:
        data.append(row)
    #dataframe of the users data
    df = pd.DataFrame(data)
    print(df)

    #for demo purposes this uses us-area-code-cities.csv
    print('Please insert file you wish to edit')
    userFile.userData = df
    
    userMenu = '0'
    #**TODO: menu loop
    while userMenu == '0':
            print("How do you wish to edit this file?")
            print("(1.)Add Row")
            print("(2.)Delete Row  - !!This will write a new file to the main folder named outfile!!")
            print("(3.)Sort file")
            print("(4.)Modify column")

            userMenu = input("Menu Input: ")
        
            if userMenu == '1':
                print("Adding row....")
                addList = addRow()
                print(addList)
            if userMenu == '2':
                print("Deleting row....")
                removeRow()
            if userMenu == '3':
                print("Sorting row....")
                sortRow(userFile)
            if userMenu == '4':
                print("Modifying row....")
                modifyColumn(userFile)

#TODO: both of these functions need to be rewritten to use the dataframe created in main.

def addRow():
    #declaring variables
    userInformation = []

    #reformat this
    for row in reader:
        rowInformation = row
        lengthHolder = int(len(row))
    
    #**holding the len of the rows so the user can set it up
    #print(lengthHolder)
    #print(rowInformation)
    for x in range(lengthHolder):
        print("***Example Column***: ",rowInformation[x])
        #*****TODO 1ST 2ND 3RD 4TH 5TH ect.*****
        print("Please Input into row number ", x+1,":")
        userInput = input('input:')
        userInformation.append(userInput)

    #adding information to csv
    with open('us-area-code-cities.csv', 'a') as nFile:
        newWriter = writer(nFile)

        newWriter.writerow(userInformation)
        nFile.close()
    return(userInformation)


    #need to rewrite this
#working
def removeRow():
    x = 0
    confirmation = False
    #container for all of the values
    csvInformation = []
    removedInformation = ''
    updatedInfo = []
    reader = csv.reader(open('us-area-code-cities.csv', encoding="utf8"))

    for row in reader:
        csvInformation.append(row)
        x+=1
    #sanitation check; to avoid ZERO
    print(len(csvInformation))
    while confirmation == False:
        userInput = int(input("Please input the row number you wish to remove"))
        print(csvInformation[userInput - 1])
        userCon = input('Is this the correct row you wish to remove (Y/N)(1/0): ')
        if userCon == '1':
            print('Removing...')
            #potenially bad
            #removedInformation.append(csvInformation[userInput - 1])
            removedInformation = csvInformation[userInput - 1]
            confirmation = True
        else:
            print('Leaving...')
            print(userCon)
            confirmation = False

    #moving information around this can be written better        
    #print('moving to row updates ', removedInformation)
    for row in csvInformation:
        #this will find all versions of that if its the same,
        #TODO:FIX CHECK SO THAT IT ERASES ONLY ONE VERSION
        if removedInformation != row:
            updatedInfo.append(row)
            
        
    print(updatedInfo)    
    #create list that contains an updated version of the users list, then write it to the file
    #CSV SHOULD BE USERS FILE
    file = open('outfile.csv', 'w+', newline='', encoding="utf-8")

    with file:
        write = csv.writer(file)
        write.writerows(updatedInfo)
    


    print(x)


#def searchRow():
#should search through the full list for a specific row the user is looking for
#can look from just the name, would prefer to have it reference the whole column in the search and display from a list
#can use weather search

def sortRow(userDataFrame):
#ask the user which row they would like to sort
        #print out one column and have them select a number to sort from [(1)973,Paterson,(2)New Jersey,(3)US,(4)40.91677,(5)-74.17181]
        print(userDataFrame.userData)

        sortedFrame = userDataFrame.userData

        ##TODO: ALLOW THE USER TO PICK WHICH COLUMN THEY WISH TO EDIT 
        #userInput = input("Please select the column number you wish to sort by")
        #columnSort = input("Which column would you like to sort by?")

        userMenu = '0'
        while userMenu == '0':

            userMenu = input("Which column would you like to sort by: ")
            try:
                sortedFrame = sortedFrame.sort_values(sortedFrame.columns[int(userMenu)])
                print(sortedFrame)
            except:
                print("Please select from one of the given column values.")

        conformationMenu = 0

        

#display sorted outfile.


def modifyColumn(userDataFrame):
    print(userDataFrame.userData)
#


    



main()
#then what?