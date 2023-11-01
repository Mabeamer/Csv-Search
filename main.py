import csv
import sys
from csv import writer
import os
import pandas as pd

#cv search function


reader = csv.reader(open('us-area-code-cities.csv', encoding="utf8"))

#display what line the user should search frm (area code example, city, state, long/lat)
#once selected have them search
#display all found references to file
#passing in placeholder***
def Search():
    ticker = 0
    numCheck = False
    #ask user to load file, will be preloading us-area-code-cities
    #print("Please load csv file for editing")

    print("Please select the column you wish to search from (Row number starts from 0)")
    #print(reader[1])
    for row in reader:
        #TODO: refactor this could be bool 
        if ticker < 1:
            print(row)
            #user makes choice here, need to find out how to keep them in bounds so they don't throw an exception
            rowInput = int(input("Row Selection: "))


            ##bounderies check
            while numCheck == False:
                try:
                    print(row[rowInput])
                    x = rowInput
                    numCheck = True
                    #**CHECK THIS, returning rowInput to keep the row number in an object.
                    return(x)
                    #move back to driver after you know what row to work in, take information to be remembered.
                except IndexError:
                    # Index Out of Bound
                    print("value doesnt exist")
                    numCheck = True
            ticker += 1

def main():
    class fileSearch:
        def __init__(self, columnSearch,):
            self.columnSearch = columnSearch

    #placeholder name
    file = fileSearch("")

    #for demo purposes this uses us-area-code-cities.csv
    print('Please insert file you wish to edit')
    file.columnSearch = Search()
    print(file.columnSearch, ' || columnSearch')

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
        if userMenu == '4':
            print("Modifying row....")


def addRow():
    #declaring variables
    userInformation = []

    #reformat this, I dont know how to pull the number correctly so will hold it in a variable to be used as the row count
    #inefficient, the loop is but we need to work around that
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
    
def removeRow():
    x = 0
    confirmation = False
    #container for all of the values
    csvInformation = []
    removedInformation = []
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
            removedInformation.append(csvInformation[userInput - 1])
            confirmation = True
        else:
            print('Leaving...')
            print(userCon)
            confirmation = False


    #about to be rewriten
    df = pd.DataFrame()

    for row in csvInformation:
        if removedInformation not in row:
            print('appending')
            df._append(row)
        if removedInformation in row:
            print("**************************************************************************")

    df = df.dropna()

    #Keep only the needed columns
    #df = df.reindex(columns=['Name', 'Location'])
    print(df.to_string())

    df.to_csv('outfile', encoding='utf-8', index=False)


    print(x)

    



main()
#then what?