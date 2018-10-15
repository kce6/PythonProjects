import re

gitc2305 = {"mall36-00": "mall36-00.njit.edu",
            "mall36-01": "mall36-01.njit.edu",
            "mall36-02": "mall36-02.njit.edu",
            "mall36-03": "mall36-03.njit.edu",
            "mall36-04": "mall36-04.njit.edu",
            "mall36-05": "mall36-05.njit.edu",
            "mall36-06": "mall36-06.njit.edu",
            "mall36-07": "mall36-07.njit.edu",
            "mall36-08": "mall36-08.njit.edu",
            "mall36-09": "mall36-09.njit.edu",
            "mall36-10": "mall36-10.njit.edu", }

gitc2302 = {"mall36-00": "mall36-00.njit.edu",
            "mall36-01": "mall36-01.njit.edu",
            "mall36-02": "mall36-02.njit.edu",
            "mall36-03": "mall36-03.njit.edu",
            "mall36-04": "mall36-04.njit.edu",
            "mall36-05": "mall36-05.njit.edu",
            "mall36-06": "mall36-06.njit.edu",
            "mall36-07": "mall36-07.njit.edu",
            "mall36-08": "mall36-08.njit.edu",
            "mall36-09": "mall36-09.njit.edu",
            "mall36-10": "mall36-10.njit.edu", }

gitc2315A = {"mall36-00": "mall36-00.njit.edu",
             "mall36-01": "mall36-01.njit.edu",
             "mall36-02": "mall36-02.njit.edu",
             "mall36-03": "mall36-03.njit.edu",
             "mall36-04": "mall36-04.njit.edu",
             "mall36-05": "mall36-05.njit.edu",
             "mall36-06": "mall36-06.njit.edu",
             "mall36-07": "mall36-07.njit.edu",
             "mall36-08": "mall36-08.njit.edu",
             "mall36-09": "mall36-09.njit.edu",
             "mall36-10": "mall36-10.njit.edu", }

gitc2315B = {"mall36-00": "mall36-00.njit.edu",
             "mall36-01": "mall36-01.njit.edu",
             "mall36-02": "mall36-02.njit.edu",
             "mall36-03": "mall36-03.njit.edu",
             "mall36-04": "mall36-04.njit.edu",
             "mall36-05": "mall36-05.njit.edu",
             "mall36-06": "mall36-06.njit.edu",
             "mall36-07": "mall36-07.njit.edu",
             "mall36-08": "mall36-08.njit.edu",
             "mall36-09": "mall36-09.njit.edu",
             "mall36-10": "mall36-10.njit.edu", }

mall36 = {"mall36-00": "mall36-00.njit.edu",
          "mall36-01": "mall36-01.njit.edu",
          "mall36-02": "mall36-02.njit.edu",
          "mall36-03": "mall36-03.njit.edu",
          "mall36-04": "mall36-04.njit.edu",
          "mall36-05": "mall36-05.njit.edu",
          "mall36-06": "mall36-06.njit.edu",
          "mall36-07": "mall36-07.njit.edu",
          "mall36-08": "mall36-08.njit.edu",
          "mall36-09": "mall36-09.njit.edu",
          "mall36-10": "mall36-10.njit.edu", }

mall37 = {"mall36-00": "mall36-00.njit.edu",
          "mall36-01": "mall36-01.njit.edu",
          "mall36-02": "mall36-02.njit.edu",
          "mall36-03": "mall36-03.njit.edu",
          "mall36-04": "mall36-04.njit.edu",
          "mall36-05": "mall36-05.njit.edu",
          "mall36-06": "mall36-06.njit.edu",
          "mall36-07": "mall36-07.njit.edu",
          "mall36-08": "mall36-08.njit.edu",
          "mall36-09": "mall36-09.njit.edu",
          "mall36-10": "mall36-10.njit.edu", }

mall38 = {"mall36-00": "mall36-00.njit.edu",
          "mall36-01": "mall36-01.njit.edu",
          "mall36-02": "mall36-02.njit.edu",
          "mall36-03": "mall36-03.njit.edu",
          "mall36-04": "mall36-04.njit.edu",
          "mall36-05": "mall36-05.njit.edu",
          "mall36-06": "mall36-06.njit.edu",
          "mall36-07": "mall36-07.njit.edu",
          "mall36-08": "mall36-08.njit.edu",
          "mall36-09": "mall36-09.njit.edu",
          "mall36-10": "mall36-10.njit.edu", }

mall39 = {"mall36-00": "mall36-00.njit.edu",
          "mall36-01": "mall36-01.njit.edu",
          "mall36-02": "mall36-02.njit.edu",
          "mall36-03": "mall36-03.njit.edu",
          "mall36-04": "mall36-04.njit.edu",
          "mall36-05": "mall36-05.njit.edu",
          "mall36-06": "mall36-06.njit.edu",
          "mall36-07": "mall36-07.njit.edu",
          "mall36-08": "mall36-08.njit.edu",
          "mall36-09": "mall36-09.njit.edu",
          "mall36-10": "mall36-10.njit.edu", }

mall40 = {"mall36-00": "mall36-00.njit.edu",
          "mall36-01": "mall36-01.njit.edu",
          "mall36-02": "mall36-02.njit.edu",
          "mall36-03": "mall36-03.njit.edu",
          "mall36-04": "mall36-04.njit.edu",
          "mall36-05": "mall36-05.njit.edu",
          "mall36-06": "mall36-06.njit.edu",
          "mall36-07": "mall36-07.njit.edu",
          "mall36-08": "mall36-08.njit.edu",
          "mall36-09": "mall36-09.njit.edu",
          "mall36-10": "mall36-10.njit.edu", }

cab1050 = {"mall36-00": "mall36-00.njit.edu",
           "mall36-01": "mall36-01.njit.edu",
           "mall36-02": "mall36-02.njit.edu",
           "mall36-03": "mall36-03.njit.edu",
           "mall36-04": "mall36-04.njit.edu",
           "mall36-05": "mall36-05.njit.edu",
           "mall36-06": "mall36-06.njit.edu",
           "mall36-07": "mall36-07.njit.edu",
           "mall36-08": "mall36-08.njit.edu",
           "mall36-09": "mall36-09.njit.edu",
           "mall36-10": "mall36-10.njit.edu", }

cab1047 = {"mall36-00": "mall36-00.njit.edu",
           "mall36-01": "mall36-01.njit.edu",
           "mall36-02": "mall36-02.njit.edu",
           "mall36-03": "mall36-03.njit.edu",
           "mall36-04": "mall36-04.njit.edu",
           "mall36-05": "mall36-05.njit.edu",
           "mall36-06": "mall36-06.njit.edu",
           "mall36-07": "mall36-07.njit.edu",
           "mall36-08": "mall36-08.njit.edu",
           "mall36-09": "mall36-09.njit.edu",
           "mall36-10": "mall36-10.njit.edu", }

Honors = {"mall36-00": "mall36-00.njit.edu",
          "mall36-01": "mall36-01.njit.edu",
          "mall36-02": "mall36-02.njit.edu",
          "mall36-03": "mall36-03.njit.edu",
          "mall36-04": "mall36-04.njit.edu",
          "mall36-05": "mall36-05.njit.edu",
          "mall36-06": "mall36-06.njit.edu",
          "mall36-07": "mall36-07.njit.edu",
          "mall36-08": "mall36-08.njit.edu",
          "mall36-09": "mall36-09.njit.edu",
          "mall36-10": "mall36-10.njit.edu", }

G12 = {"mall36-00": "mall36-00.njit.edu",
       "mall36-01": "mall36-01.njit.edu",
       "mall36-02": "mall36-02.njit.edu",
       "mall36-03": "mall36-03.njit.edu",
       "mall36-04": "mall36-04.njit.edu",
       "mall36-05": "mall36-05.njit.edu",
       "mall36-06": "mall36-06.njit.edu",
       "mall36-07": "mall36-07.njit.edu",
       "mall36-08": "mall36-08.njit.edu",
       "mall36-09": "mall36-09.njit.edu",
       "mall36-10": "mall36-10.njit.edu", }

labs = {0: "gitc2305",
        1: "gitc2302",
        2: "gitc2315A",
        3: "gitc2315B",
        4: "mall36",
        5: "mall37",
        6: "mall38",
        7: "mall39",
        8: "mall40",
        9: "cab1050",
        10: "cab1047",
        11: "Honors",
        12: "G12", }


def displayLabs(labs):
    print("List of Labs:")
    for key, value in labs.items():
        print(key, " : ", value)


def checkChars(prompt):
    while True:
        result = input(prompt).strip()
        try:
            if not result:
                raise ValueError
            elif not re.match("^[a-zA-Z]*$", result):
                raise ValueError
        except ValueError:
            print("Numbers and spaces are not allowed and the field CAN NOT be blank!")
        else:
            return result


def checkPassword(prompt):
    result = input(prompt).strip()
    try:
        if not result:
            raise ValueError
    except ValueError:
        print("Numbers and spaces are not allowed and the field CAN NOT be blank!")
    else:
        return result


def checkInt(prompt):
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            # Try again
            print("Sorry, that was not a number.  Please enter a new choice")
            continue
        else:
            return choice


def getLab():
    print("Which lab would you like to work with?")
    prompt = "Enter Lab Choice: "
    labChoice = checkInt(prompt)

    if labChoice in labs.keys():
        return labs[labChoice]
    else:
        print("That was not a valid choice.  Please enter again")
        getLab()


def getUsername():
    print("\nWhat username should I use to log into the machine?\n")
    prompt = "username: "
    username = checkChars(prompt)
    return username


def getPassword():
    print("\nWhat password should I use to log into the machine?\n")
    prompt = "password: "
    password = checkPassword(prompt)
    return password

    # Calls
displayLabs(labs)


lab = getLab()
uname = getUsername()
passwd = getPassword()

print("\n\nLab Name : %s" % lab)
print("Username : %s" % uname)
print("Password : %s" % passwd)
