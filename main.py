import csv
import sys

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
    while userMenu == '0':
        print("How do you wish to edit this file?")
        print("(1.)Add Row")
        print("(2.)Delete Row")
        print("(3.)Sort file")
        print("(4.)Modify column")

        userMenu = input("Menu Input: ")
        
        if userMenu == '1':
            print("Adding row....")
            addRow()
        if userMenu == '2':
            print("Deleting row....")
        if userMenu == '3':
            print("Sorting row....")
        if userMenu == '4':
            print("Modifying row....")


def addRow():
    print("Please insert row information")
    rowInput = input("Please insert row information")
    #fix this man
    uhh = 1
    while uhh == 1:
        for row in reader:
            uhh=2
            print(row)




main()
#then what?