################################################################################
#                       THE SYSADMIN'S USER MODIFICATION                       #
#                               AND CREATION TOOL                              #
#                                                                              #
#           This program was created to make adding, removing, or otherwise    #
#        modifying users on a *nix based system.  This program is freely       #
#        distributable and modifiable.  This is the CLI based version.  A      #
#        GUI version is in development using TKinter and will be complete soon #
#                                                                              #
################################################################################

# Imports

import os as linux
import time

# Functions


# Main Menu
def mainMenu():
    print("\nWelcome to the User Creation Service\n")
    print("Please select one of the following options: \n")
    print("1.  Create a new user with standard permissions")
    print("2.  Create a new user with advanced permissions")
    print("3.  Create a new administrator")
    print("4.  Modify the group of an existing user")
    print("5.  Remove a user")
    print("6.  Exit the program")

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
        print("You have chosen to create a new user with standard permissions\n")
        time.sleep(3)
        print("Loading new user creation interface...")
        time.sleep(3)
        newUserStandard()

    elif choice == 2:
        print("You have chosen to create a new user with advanced permissions\n")
        time.sleep(seconds=3)
        print("Loading new user creation interface...")
        time.sleep(seconds=3)
        newUserAdvanved()

    elif choice == 3:
        print("You have chosen to create a new administrator\n")
        time.sleep(3)
        print("Loading new administrator creation interface...")
        time.sleep(3)
        newAdmin()

    elif choice == 4:
        print("You have chosen to modify the group of an existing user\n")
        time.sleep(3)
        print("Loading modify group interface...")
        time.sleep(3)
        modifyGroup()

    elif choice == 5:
        print("You have chosen to remove a user\n")
        time.sleep(3)
        print("Loading remove user interface...")
        time.sleep(3)
        removeUser()

    elif choice == 6:
        print("Exiting program...")
        time.sleep(2)
        exit()

    else:
        print("That was not one of the options, please choose again")
        time.sleep(2)
        mainMenu()

def newUserStandard():
    pass

def newUserAdvanved():
    pass

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
