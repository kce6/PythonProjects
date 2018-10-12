################################################################################
#                       THE SYSADMIN'S USER CREATION                           #
#                           AND MODIFICATION TOOL                              #
#                                                                              #
#           This program was created to make adding, removing, or otherwise    #
#        modifying users on a *nix based system.  This program is freely       #
#        distributable and modifiable.  This is the CLI based version.  A      #
#        GUI version is in development using TKinter and will be complete soon #
#                                                                              #
################################################################################

# Imports

import csv
import subprocess
import time
import re

# Functions
# Main Menu
def mainMenu():
    print("\nWelcome to the User Creation Service\n")
    print("Please select one of the following options: \n")
    print("1.  Create a new user")
    print("2.  Create a new administrator")
    print("3.  Modify the group of an existing user")
    print("4.  Remove a user")
    print("5.  Exit the program")

    # try catch to ensure user is entering a number
    while True:
        try:
            choice = int(input("Enter your choice > "))
        except ValueError:
            #try again
            print("Sorry, that was not a number.  Please enter a new choice")
            continue
        else:
            #choice was successfully parsed.  exiting loop
            break

    if choice == 1:
        print("\nYou have chosen to create a new user with standard permissions")
        time.sleep(1)
        print("Loading new user creation interface...")
        time.sleep(1)
        newUser()

    elif choice == 2:
        print("\nYou have chosen to create a new administrator")
        time.sleep(1)
        print("Loading new administrator creation interface...")
        time.sleep(1)
        newAdmin()

    elif choice == 3:
        print("\nYou have chosen to modify the group of an existing user")
        time.sleep(1)
        print("Loading modify group interface...")
        time.sleep(1)
        modifyGroup()

    elif choice == 4:
        print("\nYou have chosen to remove a user")
        time.sleep(1)
        print("Loading remove user interface...")
        time.sleep(1)
        removeUser()

    elif choice == 5:
        print("\nExiting program...")
        time.sleep(1)
        exit()

    else:
        print("\nThat was not one of the options, please choose again")
        time.sleep(1)
        mainMenu()

# Sanitize User Input
def checkInput(prompt):
    while True:
        result = input(prompt).strip()
        try:
            if not result:
                raise ValueError
            if not re.match("^[ a-zA-Z]*$", result):
                raise ValueError
        except ValueError:
            print("Numbers are not allowed and the field CAN NOT be blank!")
        else:
            return result

# New User
def newUser():
    # Full Name
    print("Welcome to the New User Creation Interface\n")
    time.sleep(1)
    prompt = "First things first, what is the full name (First and Last) of the New User? > "
    fullName = checkInput(prompt)
    time.sleep(1)
    print("\nGreat! The name for the new user is: " + fullName)
    print("\n")

    # User Name
    time.sleep(1)
    prompt = """Next, what is the username of the User?  (We recommend using
first initial and full last name) > """
    userName = checkInput(prompt)
    time.sleep(1)
    print("\nGreat! The username for the new user is: " + userName)
    print("\n")

    # Group
    time.sleep(1)
    prompt = """\nNext, what group would you like the user to be added to?
(NOTE: The user will be created with a default group that is the same as their
username.  If you would like that user to be added to an additional group,
i.e. HR, Management, IT, etc., please specify it here) > """
    userGroup = checkInput(prompt)
    time.sleep(1)

    # Check to see if the group specified exisits.  If it doesn't ask user if
    # the group should be created

    groups = subprocess.Popen("getent group | cut -d: -f1", stdout=subprocess.PIPE, universal_newlines=True, stderr=None, shell=True)

    existing_groups = []
    for line in groups.stdout:
        line = line.rstrip()
        existing_groups.append(line)

    while userGroup not in existing_groups:
        print("\nThat is not an existing group.  Please enter a different group")
        time.sleep(1)
        userGroup = checkInput(prompt)

    print("\nOk, just to recap:\nFull Name: " + fullName + "\nUsername: " + userName + "\nGroup:  "+ userGroup)

    print("\nIs this information correct?")
    while True:
        correctInfo = input("(Y)es or (N)o: ").strip()
        try:
            if not correctInfo:
                raise ValueError
            if not re.match("^[yYnN]*$", correctInfo):
                raise ValueError
        except ValueError:
            print("Numbers are not allowed and the field CAN NOT be blank!")
        else:
            break

    if (correctInfo == 'y') or (correctInfo == 'Y'):
        print("Great! Creating new user now...")
        time.sleep(2)
    elif (correctInfo == 'n') or (correctInfo == 'N'):
        print("Please enter the information again")
        newUser()

def newAdmin():
    pass

def modifyGroup():
    pass

def removeUser():
    pass

def exitProgram():
    pass

#Starting the program
mainMenu()
