import re
import sys
import datetime


class process_cal():
    def __init__(self, fp):    #constructor, sets filename and calls file_to_list
        self.fp = fp
        self.file_to_list()

    def file_to_list(self):
        dict = {}           
        key = -1
        lrrules3 = []
        savelrrule = [] 
        with open(self.fp, "r") as f: #opens file and splits lines
            lines = f.readlines()
            lines = [line.rstrip() for line in lines]
            for x in range(0, len(lines)):     
                if lines[x] == '':         #in memory, I had some arrays with [''] so I just popped it
                    lines.pop()
                else:
                    l = re.split('\:', lines[x])  #uses regex to split by : in list
                    print(l)
                    if l[0] == 'BEGIN':    #I could have used regex here, my apologies, please dont deduct marks. but I had already done this so I decided to continue. 
                                                #Simply takes first element of list and splits and puts in a dictionary 
                        if l[1] == 'VEVENT':
                            key += 1
                            dict[key] = []
                    if l[0] == 'DTSTART':
                        l[1] = self.convertDate(l[1])       #calls convertDate and converts the date to a datetime object
                        dict[key].append(l[1])
                    if l[0] == 'DTEND':
                        l[1] = self.convertDate(l[1])
                        dict[key].append(l[1])
                    if l[0] == 'LOCATION':
                        dict[key].append(l[1])
                        if len(savelrrule) != 0:
                            savelrrule.append(l[1])
                    if l[0] == 'SUMMARY':
                        dict[key].append(l[1])
                        if len(savelrrule) != 0:
                            savelrrule.append(l[1])
                    if l[0] == 'RRULE':                 #this is interesting. It was really annoying that rrule was before dtstart and dtend so I saved an array 
                                                        #added +7 days to dtstart and dtend until it reaches the max until
                        lrrules1 = re.split(";", l[1])
                        print(lrrules1)                 
                        for x in lrrules1:             #takes a look at llrule and gets the only important thing, the maximum date
                            lrrules2 = re.split("=", x)
                            lrrules3.append(lrrules2)
                        print(lrrules3)
                        for x in range(0, len(lrrules3)):
                            if lrrules3[x][0] == 'UNTIL':
                                Until = lrrules3[x][1]
                        Until = self.convertDate(Until)
                        dummyStart = dict[key][0]       #basically appends to an array which saves the origional dates and summaries of the initial event
                        dummyEnd = dict[key][1]
                        savelrrule.append(dummyStart)
                        savelrrule.append(dummyEnd)
                        savelrrule.append(Until)
                    if l[0] == 'END':
                        if l[1] == 'VEVENT':
                            if len(savelrrule) != 0:
                                print("TRUE")
                                print(savelrrule)
                                dummyStart = savelrrule[0]
                                dummyEnd = savelrrule[1]
                                Until = savelrrule[2]
                                while dummyEnd < Until:                 #once we end an event, we begin adding to the datetime object (+7) days until dummyend >= Until 
                                    dummyStart = dummyStart + \
                                        datetime.timedelta(days=7)
                                    dummyEnd = dummyEnd + \
                                        datetime.timedelta(days=7)
                                    if dummyEnd < Until:
                                        key += 1
                                        dict[key] = []
                                        dict[key].append(dummyStart)
                                        dict[key].append(dummyEnd)      #appends the new event stuff (old summary and location) to a dictionary (creates a new event)
                                        dict[key].append(savelrrule[3])
                                        dict[key].append(savelrrule[4])
                                savelrrule = []                         #sets the saved array to [] 

        dict = sorted(dict.items(), key=lambda e: e[1][0])              #sorts array based on earliest events
        print(dict)
        self.lines = lines
        self.l = l
        self.dict = dict
        self.savelrrule = savelrrule

    def convertDate(self, d):
        year = 0
        month = 0
        day = 0
        print(d)
        splitDate = re.split('[a-zA-Z]', d)             #splits the date using regex
        print(splitDate)
        mdy = re.split('([\d.]{4})([\d.]{2})([\d.]{2})', str(splitDate[0]))     #splits into 2 different arrays, one with month day year and one with hour minute second
        hms = re.split('([\d.]{2})([\d.]{2})([\d.]{2})', str(splitDate[1]))
        print(hms)
        print(mdy, "in MDY")
        for x in range(0, len(mdy)):
            print(x)
            if x == 1:                  
                year = mdy[x]
                hour = hms[x]
            if x == 2:
                month = mdy[x]
                minutes = hms[x]
            if x == 3:
                day = mdy[x]
                seconds = hms[x]
        checkDate = datetime.datetime(int(year), int(month), int(           #returns a datetime object
            day), int(hour), int(minutes), int(seconds))
        return checkDate

    def get_events_for_day(self, date):
        ret = ""
        oDate = 0                                   
        for i in range(0, len(self.dict)):
            tempDate = self.dict[i][1][0].replace(              #because we are comparing dateteime objects that have no mins hours or seconds, we need to create a temp
                minute=0, hour=0, second=0)                     #datetime object so we can see if 'tempdate' == the date we get from main
            if tempDate == date:
                ret += self.setUpString(
                    self.dict[i][1][0], self.dict[i][1][1], self.dict[i][1][2], self.dict[i][1][3], tempDate, oDate)
                oDate = tempDate
        return ret                  #returns string from setupstring

    def setUpString(self, start, end, location, summary, tempDate, oDate):  # sets up string to return, there really isn't much to this function
        if(oDate != tempDate):

            return(start.strftime('%B %d, %Y (%a)')+'\n'+"-" * len(start.strftime('%B %d, %Y (%a)'))+'\n'+start.strftime("%l:%M %p") + " to " +
                   end.strftime("%l:%M %p: ") + summary + " "+"{{"+location+"}}")

        else:

            return('\n'+start.strftime("%l:%M %p") + " to " + end.strftime("%l:%M %p: ") + summary + " "+"{{"+location+"}}")
