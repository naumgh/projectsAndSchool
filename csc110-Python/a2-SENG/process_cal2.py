import sys
import datetime
import time


# function converts dtstart and dtend string to readable datetime object
def lookAtParsedFile(parsedFile):
    x = 0
    for x in range(0, len(parsedFile)):
        if(parsedFile[x][0] == 'DTSTART' or parsedFile[x][0] == 'DTEND'):
            year = ""
            month = ""
            day = ""
            hours = ""
            minutes = ""
            s_array = parsedFile[x][1].split('T')
            split_date = list(s_array[0])
            for y in range(0, len(split_date)):

                if y < 4:
                    year += split_date[y]
                if 3 < y < 6:
                    month += split_date[y]
                if y > 5:
                    day += split_date[y]
            split_time = list(s_array[1])
            for z in range(0, len(split_time) - 2):
                if(z < 2):
                    hours += split_time[z]
                elif(z > 1):
                    minutes += split_time[z]
            tempDatetime = datetime.datetime(int(year), int(
                month), int(day), int(hours), int(minutes))
            parsedFile[x][1] = tempDatetime
    return parsedFile


# functioin converts command line arguement to readable datetime object
def saveCommandLDateTime(tempCld):
    x = 0
    finalArr = []
    while x != len(tempCld):
        for y in range(0, len(tempCld[x])):
            if(y == 0):
                year = int(tempCld[x][y])
            if(y == 1):
                month = int(tempCld[x][y])
            if(y == 2):
                day = int(tempCld[x][y])

        if x == 0:
            tempDatetime = datetime.datetime(year, month, day, 0, 0)
            finalArr.append(tempDatetime)
        elif x == 1:
            tempDatetime = datetime.datetime(year, month, day, 23, 59)
            finalArr.append(tempDatetime)
        x += 1
    return finalArr


def saveCommandLD():  # function saves command line arguement times as a string
    CLDS = []
    if("--start" in sys.argv[1]):
        arr = sys.argv[1].split("=")
        arr = arr[1].split("/")
        CLDS.append(arr)
    if("--end" in sys.argv[2]):
        arr = sys.argv[2].split("=")
        arr = arr[1].split("/")
        CLDS.append(arr)
    return CLDS


def parseFile(output):  # function parses file and splits based upon :
    arr = output.split("\n")
    while('' in arr):
        arr.remove('')
    for x in range(0, len(arr)):
        if ":" in arr[x]:
            arr[x] = arr[x].split(":")

    return arr


def openFile():  # opens file and sees if arguments are correct
    if("--file=" in sys.argv[3]):
        file_name = sys.argv[3].split("=")[1]
        try:
            with open(file_name, "r") as f:
                output = f.read()
            return output
        except FileNotFoundError:
            print("the file was not found")
            sys.exit(0)
    else:
        print("your file argument is wrong")
        sys.exit(0)


# function converts until time to readable datetime object
def convertAndTakeUntil(new_b, better_array):
    year = ""
    month = ""
    day = ""
    hours = ""
    minutes = ""
    new_a = new_b.split('T')
    split_date = list(new_a[0])
    for y in range(0, len(split_date)):

        if y < 4:
            year += split_date[y]
        if 3 < y < 6:
            month += split_date[y]
        if y > 5:
            day += split_date[y]
    split_time = list(new_a[1])
    for z in range(0, len(split_time) - 2):
        if(z < 2):
            hours += split_time[z]
        elif(z > 1):
            minutes += split_time[z]
    tempDatetime = datetime.datetime(int(year), int(
        month), int(day), int(hours), int(minutes), 59)

    return tempDatetime


def lookForRrule(better_array):  # function parses if more than 1 date listed in datetime
    for x in range(0, len(better_array)):
        if better_array[x][0] == "RRULE":
            new_a = better_array[x][1].split(";")
            for y in range(0, len(new_a)):
                new_b = new_a[y].split("=")
                if new_b[0] == "UNTIL":
                    corrected_date = convertAndTakeUntil(
                        new_b[1], better_array)
            better_array[x][1] = corrected_date

    return better_array


# function gets a 'key' for each time and sorts those keys to print in chronological order
def get_key(better_array, cld):
    arrOfKeys = []
    for x in range(0, len(better_array)):
        if better_array[x][0] == "DTSTART":
            if better_array[x][1] not in arrOfKeys:
                arrOfKeys.append(better_array[x][1])

        if better_array[x][0] == "RRULE":
            sub = better_array[x][1]
            u = datetime.timedelta(days=7)
            new_date = arrOfKeys[0]
            while new_date <= sub:
                new_date = new_date + u
                arrOfKeys.append(new_date)

    arrOfKeys.sort()
    return arrOfKeys


# function compares keys with our array of info and passes relivant date, time, summary, location, etc
def reorg(better_array, keys, cld):
    new_arr = []
    unusable = []
    foundamatch = 0
    for x in range(0, len(keys)):
        new_arr = []
        for y in range(0, len(better_array)):

            if better_array[y][0] == 'DTSTART' and better_array[y][1] == keys[x]:
                if cld[0] <= keys[x] <= cld[1]:
                    foundamatch = 1
                    new_arr.append(better_array[y][1])
                    new_arr.append(better_array[y+1][1])
                    if better_array[y+2][0] != 'RRULE':
                        new_arr.append(better_array[y+2][1])
                        new_arr.append(better_array[y+3][1])
                    elif(better_array[y+2][0] == 'RRULE'):
                        new_arr.append(better_array[y+3][1])
                        new_arr.append(better_array[y+4][1])

            if better_array[y][0] == 'END' and better_array[y][1] == 'VCALENDAR' and new_arr != []:
                # unusable used to not print new date each time passed to dump print
                unusable = dump_print(new_arr, unusable)
                new_arr = []


def dump_print(new_arr, unusable):
    dtobject = new_arr[0]
    # prints data onto stdout in correct format
    new_date = dtobject.replace(minute=0, second=0)
    if new_date not in unusable:
        print(new_date.strftime("%B" " %d," " %Y" " (%a)"))
        print('-' * len(new_date.strftime("%B" " %d," " %Y" " (%a)")))
        unusable.append(new_date)
    if new_arr != []:
        print(new_arr[0].strftime("%#I:%M %p")+" to " + new_arr[1].strftime("%#I:%M %p") +
              ":" + " " + new_arr[3] + " " + "{{" + new_arr[2] + "}}" + "\n")
        new_arr = []

    return unusable


def main():
    f = openFile()
    parsedFile = parseFile(f)
    tempCld = saveCommandLD()
    cld = saveCommandLDateTime(tempCld)
    better_array = lookAtParsedFile(parsedFile)
    better_array = lookForRrule(better_array)
    keys = get_key(better_array, cld)
    reorg(better_array, keys, cld)


if __name__ == '__main__':
    main()
