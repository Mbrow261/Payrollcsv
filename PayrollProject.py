import csv


def main():
    while True:
        mainMenu()
        break


def mainMenu():
    print("Choose an option for the file:" + "\n")
    print("1: Read Payroll")
    print("2: Add employee")
    print("3: Edit All Employee Info")
    print("4: Edit First Name")
    print("5: Edit Last Name")
    print("6: Edit Salary")
    print("7: Edit Zipcode")
    print("8: Delete Row")
    print("9: Exit")

    while True:
        userChoice = input("Choose an option:")
        if userChoice == '1':
            readpayroll()
            break
        elif userChoice == '2':
            addEmployee()
            break
        elif userChoice == '3':
            editAllFields()
            break
        elif userChoice == '4':
            editfirstName()
            break
        elif userChoice == '5':
            editLastName()
            break
        elif userChoice == '6':
            editSalary()
            break
        elif userChoice == '7':
            editZipcode()
            break
        elif userChoice == '8':
            deleteRow()
            break
        elif userChoice == '9':
            exit()


def addEmployee():
    userFirstName = input("What is the first name")
    userLastName = input("What is the last name")
    raw_userSalary = input("What is the salary")
    userSalary = int(raw_userSalary)
    raw_userZipcode = input("What is the Zipcode")
    userZipcode = int(raw_userZipcode)

    header = ['firstname', 'lastname', 'salary', 'zipcode']
    data = {'firstname': userFirstName, 'lastname': userLastName, 'salary': userSalary, 'zipcode': int(userZipcode)}

    with open('payroll.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)

        # write the header
        # writer.writeheader()

        # write the data
        writer.writerow(data)
        f.close()

        while True:
            userChoice = input("Would you like to view payroll Y/N? ")
            if userChoice == 'y':
                    readpayroll()
            elif userChoice == 'n':
                returnToMainMenu("Employee added")


def readpayroll():
    fieldnames = ['country name', 'area', 'code2', 'code3']
    with open('payroll.csv', encoding="utf8") as f:
        csv_reader = csv.DictReader(f)

        line = []
        for line in csv_reader:
            print(line)

    returnToMainMenu("File has been read")


def returnToMainMenu(message):
    while True:
        print()
        back = input(f"{message}.Press (B) to go back to Main Menu").lower()
        if back == "b":
            main()


def editAllFields():
    mylist = []
    with open('payroll.csv', 'r') as f:
        myfile = csv.reader(f)
        for row in myfile:
            mylist.append(row)

    print("See details below")
    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))
    editrow = int(input("\nWhich row would you like to change? Enter 1- " + str(len(mylist) - 1) + ": "))
    print("Please enter new details for the following")

    for i in range(len(mylist[0])):
        newDetails = input("Enter new detials for " + str(mylist[0][i]) + ": ")
        mylist[editrow][i] = newDetails

    print("See details of new file below")
    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))

    changeCSV = input("\n Would you like to change csvfile? Y/N ").lower()

    if changeCSV == ("y"):
        with open('payroll.csv', 'w+', newline='', encoding='utf-8') as file:
            myFile = csv.writer(file)
            for i in range(len(mylist)):
                myFile.writerow(mylist[i])
    returnToMainMenu("File has been edited")


def editLastName():

    mylist = []
    with open('payroll.csv', 'r') as f:
        myfile = csv.reader(f)
        for row in myfile:
            mylist.append(row)

    print("See details below")

    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))
    editrow = int(input("\nWhich row would you like to change? Enter 1- " + str(len(mylist) - 1) + ": "))
    print("Please enter new details for the following")

    for i in range(len(mylist[0])):
        newDetails = input("Enter new detials for " + str(mylist[0][1]) + ": ")
        mylist[editrow][1] = newDetails
        break

    print("See details of new file below")
    for i in range(len(mylist)):
       print("Row " + str(i) + ":" + str(mylist[i]))

    changeCSV = input("\n Would you like to change csvfile? Y/N ").lower()

    if changeCSV == ("y"):
        with open('payroll.csv', 'w+', newline='', encoding='utf-8') as file:
            myFile = csv.writer(file)
            for i in range(len(mylist)):
                myFile.writerow(mylist[i])

    returnToMainMenu("File has been edited")


def editfirstName():
    mylist = []
    with open('payroll.csv', 'r') as f:
        myfile = csv.reader(f)
        for row in myfile:
            mylist.append(row)

    print("See details below")

    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))
    editrow = int(input("\nWhich row would you like to change? Enter 1- " + str(len(mylist) - 1) + ": "))
    print("Please enter new details for the following")

    for i in range(len(mylist[0])):
        newDetails = input("Enter new detials for " + str(mylist[0][0]) + ": ")
        mylist[editrow][0] = newDetails
        break

    print("See details of new file below")
    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))

    changeCSV = input("\n Would you like to change csvfile? Y/N ").lower()

    if changeCSV == ("y"):
        with open('payroll.csv', 'w+', newline='', encoding='utf-8') as file:
            myFile = csv.writer(file)
            for i in range(len(mylist)):
                myFile.writerow(mylist[i])

    returnToMainMenu("File has been edited")


def editSalary():
    mylist = []
    with open('payroll.csv', 'r') as f:
        myfile = csv.reader(f)
        for row in myfile:
            mylist.append(row)

    print("See details below")

    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))
    editrow = int(input("\nWhich row would you like to change? Enter 1- " + str(len(mylist) - 1) + ": "))
    print("Please enter new details for the following")

    for i in range(len(mylist[0])):
        newDetails = input("Enter new detials for " + str(mylist[0][2]) + ": ")
        mylist[editrow][2] = newDetails
        break

    print("See details of new file below")
    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))

    changeCSV = input("\n Would you like to change csvfile? Y/N ").lower()

    if changeCSV == ("y"):
        with open('payroll.csv', 'w+', newline='', encoding='utf-8') as file:
            myFile = csv.writer(file)
            for i in range(len(mylist)):
                myFile.writerow(mylist[i])

    returnToMainMenu("File has been edited")


def editZipcode():
    mylist = []
    with open('payroll.csv', 'r') as f:
        myfile = csv.reader(f)
        for row in myfile:
            mylist.append(row)

    print("See details below")

    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))
    editrow = int(input("\nWhich row would you like to change? Enter 1- " + str(len(mylist) - 1) + ": "))
    print("Please enter new details for the following")

    for i in range(len(mylist[0])):
        newDetails = input("Enter new detials for " + str(mylist[0][3]) + ": ")
        mylist[editrow][3] = newDetails
        break

    print("See details of new file below")
    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))

    changeCSV = input("\n Would you like to change csvfile? Y/N ").lower()

    if changeCSV == ("y"):
        with open('payroll.csv', 'w+', newline='', encoding='utf-8') as file:
            myFile = csv.writer(file)
            for i in range(len(mylist)):
                myFile.writerow(mylist[i])

    returnToMainMenu("File has been edited")

def deleteRow():
    # 1. This code snippet asks the user for a username and deletes the user's record from file.
    mylist = []
    with open('payroll.csv', 'r') as f:
        myfile = csv.reader(f)
        for row in myfile:
            mylist.append(row)

    print("See details below")

    for i in range(len(mylist)):
        print("Row " + str(i) + ":" + str(mylist[i]))
        f.close()
    updatedlist = []
    with open("payroll.csv", newline="") as f:
        reader = csv.reader(f)
        firstname = input("Enter the firstname of the user you wish to remove from file:")

        for row in reader:  # for every row in the file

            if row[0] != firstname:  # as long as the username is not in the row .......
                updatedlist.append(row)  # add each row, line by line, into a list called 'udpatedlist'
        print(updatedlist)
        updatefile(updatedlist)
        mylist=[]
        with open('payroll.csv', 'r') as f:
            myfile = csv.reader(f)
            for row in myfile:
                mylist.append(row)

        print("See details below")

        for i in range(len(mylist)):
            print("Row " + str(i) + ":" + str(mylist[i]))


def updatefile(updatedlist):
    with open("payroll.csv", "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")

main()
