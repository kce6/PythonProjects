import re

labs = {"2302": {"labName": "2302", "station0": "2302-00", "hostname0": "2302-00.njit.edu",
                 "station1": "2302-01", "hostname1": "2302-01.njit.edu",
                 "station2": "2302-02", "hostname2": "2302-02.njit.edu",
                 "station3": "2302-03", "hostname3": "2302-03.njit.edu",
                 "station4": "2302-04", "hostname4": "2302-04.njit.edu",
                 "station5": "2302-05", "hostname5": "2302-05.njit.edu",
                 "station6": "2302-06", "hostname6": "2302-06.njit.edu",
                 "station6": "2302-07", "hostname7": "2302-07.njit.edu",
                 "station7": "2302-08", "hostname8": "2302-08.njit.edu",
                 "station8": "2302-09", "hostname9": "2302-09.njit.edu",
                 "station9": "2302-10", "hostname10": "2302-10.njit.edu"},
        "2305": {"labName": "2305", "station0": "2305-00", "hostname0": "2305-00.njit.edu",
                 "station1": "2305-01", "hostname1": "2305-01.njit.edu",
                 "station2": "2305-02", "hostname2": "2305-02.njit.edu",
                 "station3": "2305-03", "hostname3": "2305-03.njit.edu",
                 "station4": "2305-04", "hostname4": "2305-04.njit.edu",
                 "station5": "2305-05", "hostname5": "2305-05.njit.edu",
                 "station6": "2305-06", "hostname6": "2305-06.njit.edu",
                 "station6": "2305-07", "hostname7": "2305-07.njit.edu",
                 "station7": "2305-08", "hostname8": "2305-08.njit.edu",
                 "station8": "2305-09", "hostname9": "2305-09.njit.edu",
                 "station9": "2305-10", "hostname10": "2305-10.njit.edu"},
        "2315A": {"labName": "2315A", "station0": "2315A-00", "hostname0": "2315A-00.njit.edu",
                  "station1": "2315A-01", "hostname1": "2315A-01.njit.edu",
                  "station2": "2315A-02", "hostname2": "2315A-02.njit.edu",
                  "station3": "2315A-03", "hostname3": "2315A-03.njit.edu",
                  "station4": "2315A-04", "hostname4": "2315A-04.njit.edu",
                  "station5": "2315A-05", "hostname5": "2315A-05.njit.edu",
                  "station6": "2315A-06", "hostname6": "2315A-06.njit.edu",
                  "station6": "2315A-07", "hostname7": "2315A-07.njit.edu",
                  "station7": "2315A-08", "hostname8": "2315A-08.njit.edu",
                  "station8": "2315A-09", "hostname9": "2315A-09.njit.edu",
                  "station9": "2315A-10", "hostname10": "2315A-10.njit.edu"},
        "2315B": {"labName": "2315B", "station0": "2315B-00", "hostname0": "2315B-00.njit.edu",
                  "station1": "2315B-01", "hostname1": "2315B-01.njit.edu",
                  "station2": "2315B-02", "hostname2": "2315B-02.njit.edu",
                  "station3": "2315B-03", "hostname3": "2315B-03.njit.edu",
                  "station4": "2315B-04", "hostname4": "2315B-04.njit.edu",
                  "station5": "2315B-05", "hostname5": "2315B-05.njit.edu",
                  "station6": "2315B-06", "hostname6": "2315B-06.njit.edu",
                  "station6": "2315B-07", "hostname7": "2315B-07.njit.edu",
                  "station7": "2315B-08", "hostname8": "2315B-08.njit.edu",
                  "station8": "2315B-09", "hostname9": "2315B-09.njit.edu",
                  "station9": "2315B-10", "hostname10": "2315B-10.njit.edu"},
        "mall36": {"labName": "mall36", "station0": "mall36-00", "hostname0": "mall36-00.njit.edu",
                   "station1": "mall36-01", "hostname1": "mall36-01.njit.edu",
                   "station2": "mall36-02", "hostname2": "mall36-02.njit.edu",
                   "station3": "mall36-03", "hostname3": "mall36-03.njit.edu",
                   "station4": "mall36-04", "hostname4": "mall36-04.njit.edu",
                   "station5": "mall36-05", "hostname5": "mall36-05.njit.edu",
                   "station6": "mall36-06", "hostname6": "mall36-06.njit.edu",
                   "station6": "mall36-07", "hostname7": "mall36-07.njit.edu",
                   "station7": "mall36-08", "hostname8": "mall36-08.njit.edu",
                   "station8": "mall36-09", "hostname9": "mall36-09.njit.edu",
                   "station9": "mall36-10", "hostname10": "mall36-10.njit.edu"},
        "mall37": {"labName": "mall37", "station0": "mall37-00", "hostname0": "mall37-00.njit.edu",
                   "station1": "mall37-01", "hostname1": "mall37-01.njit.edu",
                   "station2": "mall37-02", "hostname2": "mall37-02.njit.edu",
                   "station3": "mall37-03", "hostname3": "mall37-03.njit.edu",
                   "station4": "mall37-04", "hostname4": "mall37-04.njit.edu",
                   "station5": "mall37-05", "hostname5": "mall37-05.njit.edu",
                   "station6": "mall37-06", "hostname6": "mall37-06.njit.edu",
                   "station6": "mall37-07", "hostname7": "mall37-07.njit.edu",
                   "station7": "mall37-08", "hostname8": "mall37-08.njit.edu",
                   "station8": "mall37-09", "hostname9": "mall37-09.njit.edu",
                   "station9": "mall37-10", "hostname10": "mall37-10.njit.edu"},
        "mall38": {"labName": "mall38", "station0": "mall38-00", "hostname0": "mall38-00.njit.edu",
                   "station1": "mall38-01", "hostname1": "mall38-01.njit.edu",
                   "station2": "mall38-02", "hostname2": "mall38-02.njit.edu",
                   "station3": "mall38-03", "hostname3": "mall38-03.njit.edu",
                   "station4": "mall38-04", "hostname4": "mall38-04.njit.edu",
                   "station5": "mall38-05", "hostname5": "mall38-05.njit.edu",
                   "station6": "mall38-06", "hostname6": "mall38-06.njit.edu",
                   "station6": "mall38-07", "hostname7": "mall38-07.njit.edu",
                   "station7": "mall38-08", "hostname8": "mall38-08.njit.edu",
                   "station8": "mall38-09", "hostname9": "mall38-09.njit.edu",
                   "station9": "mall38-10", "hostname10": "mall38-10.njit.edu"},
        "mall39": {"labName": "mall39", "station0": "mall39-00", "hostname0": "mall39-00.njit.edu",
                   "station1": "mall39-01", "hostname1": "mall39-01.njit.edu",
                   "station2": "mall39-02", "hostname2": "mall39-02.njit.edu",
                   "station3": "mall39-03", "hostname3": "mall39-03.njit.edu",
                   "station4": "mall39-04", "hostname4": "mall39-04.njit.edu",
                   "station5": "mall39-05", "hostname5": "mall39-05.njit.edu",
                   "station6": "mall39-06", "hostname6": "mall39-06.njit.edu",
                   "station6": "mall39-07", "hostname7": "mall39-07.njit.edu",
                   "station7": "mall39-08", "hostname8": "mall39-08.njit.edu",
                   "station8": "mall39-09", "hostname9": "mall39-09.njit.edu",
                   "station9": "mall39-10", "hostname10": "mall39-10.njit.edu"},
        "mall40": {"labName": "mall40", "station0": "mall40-00", "hostname0": "mall40-00.njit.edu",
                   "station1": "mall40-01", "hostname1": "mall40-01.njit.edu",
                   "station2": "mall40-02", "hostname2": "mall40-02.njit.edu",
                   "station3": "mall40-03", "hostname3": "mall40-03.njit.edu",
                   "station4": "mall40-04", "hostname4": "mall40-04.njit.edu",
                   "station5": "mall40-05", "hostname5": "mall40-05.njit.edu",
                   "station6": "mall40-06", "hostname6": "mall40-06.njit.edu",
                   "station6": "mall40-07", "hostname7": "mall40-07.njit.edu",
                   "station7": "mall40-08", "hostname8": "mall40-08.njit.edu",
                   "station8": "mall40-09", "hostname9": "mall40-09.njit.edu",
                   "station9": "mall40-10", "hostname10": "mall40-10.njit.edu"},
        "cab1047": {"labName": "cab1047", "station0": "cab1047-00", "hostname0": "cab1047-00.njit.edu",
                    "station1": "cab1047-01", "hostname1": "cab1047-01.njit.edu",
                    "station2": "cab1047-02", "hostname2": "cab1047-02.njit.edu",
                    "station3": "cab1047-03", "hostname3": "cab1047-03.njit.edu",
                    "station4": "cab1047-04", "hostname4": "cab1047-04.njit.edu",
                    "station5": "cab1047-05", "hostname5": "cab1047-05.njit.edu",
                    "station6": "cab1047-06", "hostname6": "cab1047-06.njit.edu",
                    "station6": "cab1047-07", "hostname7": "cab1047-07.njit.edu",
                    "station7": "cab1047-08", "hostname8": "cab1047-08.njit.edu",
                    "station8": "cab1047-09", "hostname9": "cab1047-09.njit.edu",
                    "station9": "cab1047-10", "hostname10": "cab1047-10.njit.edu"},
        "cab1050": {"labName": "cab1050", "station0": "cab1050-00", "hostname0": "cab1050-00.njit.edu",
                    "station1": "cab1050-01", "hostname1": "cab1050-01.njit.edu",
                    "station2": "cab1050-02", "hostname2": "cab1050-02.njit.edu",
                    "station3": "cab1050-03", "hostname3": "cab1050-03.njit.edu",
                    "station4": "cab1050-04", "hostname4": "cab1050-04.njit.edu",
                    "station5": "cab1050-05", "hostname5": "cab1050-05.njit.edu",
                    "station6": "cab1050-06", "hostname6": "cab1050-06.njit.edu",
                    "station6": "cab1050-07", "hostname7": "cab1050-07.njit.edu",
                    "station7": "cab1050-08", "hostname8": "cab1050-08.njit.edu",
                    "station8": "cab1050-09", "hostname9": "cab1050-09.njit.edu",
                    "station9": "cab1050-10", "hostname10": "cab1050-10.njit.edu"},
        "Honors": {"labName": "Honors", "station0": "Honors-00", "hostname0": "Honors-00.njit.edu",
                   "station1": "Honors-01", "hostname1": "Honors-01.njit.edu",
                   "station2": "Honors-02", "hostname2": "Honors-02.njit.edu",
                   "station3": "Honors-03", "hostname3": "Honors-03.njit.edu",
                   "station4": "Honors-04", "hostname4": "Honors-04.njit.edu",
                   "station5": "Honors-05", "hostname5": "Honors-05.njit.edu",
                   "station6": "Honors-06", "hostname6": "Honors-06.njit.edu",
                   "station6": "Honors-07", "hostname7": "Honors-07.njit.edu",
                   "station7": "Honors-08", "hostname8": "Honors-08.njit.edu",
                   "station8": "Honors-09", "hostname9": "Honors-09.njit.edu",
                   "station9": "Honors-10", "hostname10": "Honors-10.njit.edu"},
        "G12": {"labName": "G12", "station0": "G12-00", "hostname0": "G12-00.njit.edu",
                "station1": "G12-01", "hostname1": "G12-01.njit.edu",
                "station2": "G12-02", "hostname2": "G12-02.njit.edu",
                "station3": "G12-03", "hostname3": "G12-03.njit.edu",
                "station4": "G12-04", "hostname4": "G12-04.njit.edu",
                "station5": "G12-05", "hostname5": "G12-05.njit.edu",
                "station6": "G12-06", "hostname6": "G12-06.njit.edu",
                "station6": "G12-07", "hostname7": "G12-07.njit.edu",
                "station7": "G12-08", "hostname8": "G12-08.njit.edu",
                "station8": "G12-09", "hostname9": "G12-09.njit.edu",
                "station9": "G12-10", "hostname10": "G12-10.njit.edu"}}


def displayLabs(labs):
    print("List of Labs:")
    counter = 0
    for lab_id, lab_info in labs.items():
        print(counter, " : ", lab_id)
        counter = counter + 1
    print("Total Number of Labs: ", counter)


def checkChars(prompt):
    while True:
        result = input(prompt).strip()
        try:
            if not result:
                raise ValueError
            elif not re.match("^[a-zA-Z0-9]*$", result):
                raise ValueError
        except ValueError:
            print("Spaces are not allowed and the field CAN NOT be blank!")
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


def getLabChoice():
    print("Which lab would you like to work with? (Enter Lab Name)")
    prompt = "Enter Lab Choice: "
    labChoice = checkChars(prompt)
    return labChoice


def validateLabChoice(lab):
    for i in lab.keys():
        for labName in lab[i]:
            print(labName)


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


def getWorkstations(labs):
    pass


def main():
    displayLabs(labs)
    labToCheck = getLabChoice()
    validateLabChoice(labs)
    uname = getUsername()
    passwd = getPassword()

    print("\n\nLab Name : %s" % workingLab)
    print("Username : %s" % uname)
    print("Password : %s" % passwd)


# Calls
main()
