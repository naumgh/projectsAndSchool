#!/usr/bin/env python3
import psycopg2
from datetime import datetime
from datetime import date
from decimal import Decimal
from psycopg2 import Date
import calendar

dbconn = psycopg2.connect(host='studentdb.csc.uvic.ca',
        user='c370_s053',
        password='S6BqXNAW')

cursors = {}

for x in range(0, 15):
    cursors["cursor" + str(x)] = dbconn.cursor()


class phaseFive:    #inserting into donates
    def __init__(self):
        self.campaigns = {}
        self.donator = {}
        self.donates = {}
        self.question = {'y','n'}
    def p5_question(self):
        while True:
            check_me = input("press y and [ENTER] re-run queries, or n and [ENTER] to go back to main-menu: ")
            if check_me.lower() not in self.question:
                print("please select y or n")
            else:
                return check_me
    def printCampaign(sef):
        print("------CAMPAIGN QUERY--------")
        cursors['cursor1'].execute("""
        select * from CAMPAIGN
        """)
        for row in cursors['cursor1'].fetchall():
            print("%s %s %s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4], row[5],row[6]))
    def queryCampaign(self):
        cursors['cursor1'].execute("""
        select * from CAMPAIGN
        """)
        return cursors['cursor1'].fetchall()
    def convertCampaignToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            possibleParticipates.append(row[6])
            self.campaigns[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.campaigns
    def queryDonates(self):
        cursors['cursor2'].execute("""
        select * from DONATES
        """)
        return cursors['cursor2'].fetchall()
    def printDonates(self):
        print("------DONATES QUERY--------")
        cursors['cursor2'].execute("""
        select * from DONATES
        """)
        for row in cursors['cursor2'].fetchall():
            print("%s %s %s " % (row[0],row[1],row[2]))
    def convertDonatesToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            self.donates[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.donates
    def queryDonator(self):
        cursors['cursor2'].execute("""
        select * from DONATOR
        """)
        return cursors['cursor2'].fetchall()
    def printDonator(self):
        print("------DONATOR QUERY--------")
        cursors['cursor2'].execute("""
        select * from DONATOR
        """)
        for row in cursors['cursor2'].fetchall():
            print("%s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4]))
    def convertDonatorToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            self.donator[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.donator
    
    def insertIntoDonatesTable(self):
        selectedKeys = []
        vol_arr = self.donator.keys()
        campaign_arr = self.campaigns.keys()
        try:
            chooseDID = input("Please choose a donator id to assign to a campaign: ")
            chooseDID = int(chooseDID)
            chooseCID = input("Please choose a corresponding campaign to assign donator: ")
            chooseCID = int(chooseCID)
            total = input("Please choose a donation amount: ")
            total= int(total)
        except ValueError:
            print("please make sure you select an integer for both")
        if chooseDID in vol_arr:
            print("this volunteer is indeed in the DB")
            selectedKeys.append(chooseDID)
        else:
            print("please select a volunteer in the DB")
        if chooseCID in campaign_arr:
            print("this campaign is indeed in the DB")
            selectedKeys.append(chooseCID)
        else:
            print("please select a campaign in the DB")
        
        tuple_data = (chooseCID, chooseDID, total)
        campaign_data = [tuple_data]
        campsql = """
        INSERT INTO DONATES (CID,DID,total) VALUES (%s, %s, %s)
        ON CONFLICT (CID, DID) DO UPDATE
        SET total = DONATES.total + EXCLUDED.total
        """
        try:
            cursors['cursor6'].executemany(campsql, campaign_data)
            dbconn.commit()
            print("inserted successfully")
        except psycopg2.Error as e:
            dbconn.rollback()
            print("there was an error inserting this participant. it may already exist")
            print(e)



class phaseFour:
    def __init__(self):
        self.options = {1,2}
        self.options2 = {1, 2, 3, 4}
        self.volunteers = {}
        self.participates = {}
        self.event = {}
        self.campaign = {}
        self.phase = {}

    
    def addCampaignAnnotations(self,campaign):
        selectedKeys = []
        campaign_arr = campaign.keys()

        annotation = input("please write your annotation here: ")
        try:
            chooseCID = input("Please choose a corresponding campaign to update annotation: ")
            chooseCID = int(chooseCID)
        except ValueError:
            print("please make sure you select an integer")
        if chooseCID in campaign_arr:
            print("this campaign is indeed in the DB")
            selectedKeys.append(chooseCID)
        else:
            print("please select a campaign in the DB")
        
        tuple_data = (annotation,chooseCID)
        campaign_data = [tuple_data]
        campsql = """
            UPDATE CAMPAIGN 
            SET CampaignAnnotation = %s
            WHERE CID = %s
        """
        try:
            cursors['cursor6'].executemany(campsql, campaign_data)
            dbconn.commit()
            print("inserted successfully")
        except psycopg2.Error as e:
            dbconn.rollback()
            print("there was an error inserting in this campaign. it may already exist")
            print(e)

    def addPhaseAnnotations(self, phase):
        selectedKeys = []
        phase_arr = phase.keys()

        annotation = input("please write your annotation here: ")
        try:
            chooseCID = input("Please choose a corresponding PID to update annotation: ")
            chooseCID = int(chooseCID)
        except ValueError:
            print("please make sure you select an integer")
        if chooseCID in phase_arr:
            print("this phase is indeed in the DB")
            selectedKeys.append(chooseCID)
        else:
            print("please select a phase in the DB")
        
        tuple_data = (annotation, chooseCID)
        campaign_data = [tuple_data]
        campsql = """
            UPDATE PHASE 
            SET phaseAnnotation = %s
            WHERE phaseID = %s
        """
        try:
            cursors['cursor6'].executemany(campsql, campaign_data)
            dbconn.commit()
            print("inserted successfully")
        except psycopg2.Error as e:
            dbconn.rollback()
            print("there was an error inserting in this phase. it may already exist")
            print(e)
    
    def addEventAnnotations(self,event):
        selectedKeys = []
        phase_arr =  event.keys()

        annotation = input("please write your annotation here: ")
        try:
            chooseCID = input("Please choose a corresponding event to update annotation: ")
            chooseCID = int(chooseCID)
        except ValueError:
            print("please make sure you select an integer")
        if chooseCID in phase_arr:
            print("this event is indeed in the DB")
            selectedKeys.append(chooseCID)
        else:
            print("please select an event in the DB")
        
        tuple_data = (annotation,chooseCID)
        campaign_data = [tuple_data]
        campsql = """
            UPDATE EVENT
            SET EventAnnotation = %s
            WHERE EVID = %s
        """
        try:
            cursors['cursor6'].executemany(campsql, campaign_data)
            dbconn.commit()
            print("inserted successfully")
        except psycopg2.Error as e:
            dbconn.rollback()
            print("there was an error inserting in this event. it may already exist")
            print(e)

    def addParticipatesAnnotations(self, participates,campaign):
        selectedKeys = []
        phase_arr = self.volunteers.keys()
        selectedKeys = []
        campaign_arr = self.campaign.keys()
        print(phase_arr)
        print(campaign_arr)

        annotation = input("please write your annotation here: ")
        try:
            chooseVID = input("Please choose a volunteer to assign to a campaign by selecting their id: ")
            chooseVID = int(chooseVID)
            chooseCID = input("Please choose a corresponding campaign to assign the volunteer: ")
            chooseCID = int(chooseCID)
        except ValueError:
            print("please make sure you select an integer for both")
        if chooseVID in phase_arr:
            print("this volunteer is indeed in the DB")
            selectedKeys.append(chooseVID)
        else:
            print("please select a volunteer in the DB")
        if chooseCID in campaign_arr:
            print("this campaign is indeed in the DB")
            selectedKeys.append(chooseCID)
        else:
            print("please select a campaign in the DB")
        if len(selectedKeys) == 2:
            tuple_data = (annotation, chooseCID, chooseVID)
            campaign_data = [tuple_data]
            campsql = """
                UPDATE PARTICIPATES
                SET ParticipantAnnotation= %s
                WHERE CID = %s and VID = %s
            """
            try:
                cursors['cursor6'].executemany(campsql, campaign_data)
                dbconn.commit()
                print("inserted successfully")
            except psycopg2.Error as e:
                dbconn.rollback()
                print("there was an error inserting this participant. it may already exist")
                print(e)
        else:
            print("couldn't update due to missing CID or VID")
    
    def display2(self):
        print("Press 1 and [ENTER] to add annotations to campaign")
        print("Press 2 and [ENTER] to add annotations to phase")
        print("Press 3 and [ENTER] to add annotations to event")
        print("Press 4 and [ENTER] to add annotations to participates")
        print("Press x and [ENTER] to add go back to menu")
        p4 = input("press [ENTER] for any of these options")
        try:
            if p4.lower() == 'x':
                print("exiting")
                return 'x'
            if int(p4) in self.options2:
                return int(p4)
            else:
                print("please select a number from the list of options")
        except ValueError:
            print("make sure your selection is an integer")
    
    def display(self):
        print("Press 1 and [ENTER] to get member records/history")
        print("Press 2 and [ENTER] add annotations")
        p4 = input("press [ENTER] for any of these options")
        try:
            if p4.lower() == 'x':
                print("exiting")
                return 'x'
            if int(p4) in self.options:
                return int(p4)
            else:
                print("please select a number from the list of options")
        except ValueError:
            print("make sure your selection is an integer")

    def run(self):
        bool = True
        while bool:
            inpoot = input("Please select a list of volunteers to get history of seperated by commas. ex: 1,3,10 \nyou can also press x then [ENTER] to quit at any time: ")
            inpoot = inpoot.split(',')
            try:
                for x in range(0,len(inpoot)):
                    if inpoot[x].lower() == "x":
                        break
                    elif int(inpoot[x]) not in self.volunteers:
                        print(int(inpoot[x]), "is not in the volunteers table")
                    else:
                        inpoot[x] = int(inpoot[x])
            except ValueError:
                print(x, "is a non-integer include only integers.")
            
            return inpoot
    
    def getMembershipHistory(self, VID):
        query = """
        select * from volunteer join participates on(volunteer.VID = participates.VID)
        where volunteer.VID = %s
        """
        cursors['cursor12'].execute(query,(VID,))
        
        for row in cursors['cursor12'].fetchall():
            print("%s %s %s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4],row[5],row[7]))
    
    def printVolunteer(sef):
        print("------VOLUNTEER QUERY--------")
        cursors['cursor14'].execute("""
        select * from VOLUNTEER
        """)
        for row in cursors['cursor14'].fetchall():
            print("%s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4]))
    def queryVolunteer(self):
        cursors['cursor14'].execute("""
        select * from VOLUNTEER
        """)
        return cursors['cursor14'].fetchall()
    def convertVolunteerToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            self.volunteers[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.volunteers
    def printParticipates(sef):
        print("------PARTICIPATES--------")
        cursors['cursor14'].execute("""
        select * from PARTICIPATES
        """)
        for row in cursors['cursor14'].fetchall():
            print("%s %s %s %s %s %s" % (row[0],row[1],row[2],row[3],row[4],row[5]))
    def queryParticipates(self):
        cursors['cursor14'].execute("""
        select * from PARTICIPATES
        """)
        return cursors['cursor14'].fetchall()
    def convertParticipatesToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            self.participates[row[0],row[1]] = possibleParticipates
            possibleParticipates = []
        return self.participates
    def printEvent(sef):
        print("------EVENT QUERY--------")
        cursors['cursor14'].execute("""
        select * from EVENT
        """)
        for row in cursors['cursor14'].fetchall():
            print("%s %s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4],row[5]))
    def queryEvent(self):
        cursors['cursor14'].execute("""
        select * from EVENT
        """)
        return cursors['cursor14'].fetchall()
    def convertEventToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            self.event[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.event
    def printCampaign(sef):
        print("------CAMPAIGN QUERY--------")
        cursors['cursor14'].execute("""
        select * from CAMPAIGN
        """)
        for row in cursors['cursor14'].fetchall():
            print("%s %s %s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    def queryCampaign(self):
        cursors['cursor14'].execute("""
        select * from CAMPAIGN
        """)
        return cursors['cursor14'].fetchall()
    def convertCampaignToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            possibleParticipates.append(row[6])
            self.campaign[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.campaign
    def printPhase(sef):
        print("------PHASE QUERY--------")
        cursors['cursor14'].execute("""
        select * from PHASE
        """)
        for row in cursors['cursor14'].fetchall():
            print("%s %s %s %s %s %s" % (row[0],row[1],row[2],row[3],row[4],row[5]))
    def queryPhase(self):
        cursors['cursor14'].execute("""
        select * from PHASE
        """)
        return cursors['cursor14'].fetchall()
    def convertPhaseToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            self.phase[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.phase


class phaseThree:
    def __init__(self):
        self.campaigns={}
        self.money = []
        self.question = {'y','n'}
    def p3_question(self):
        while True:
            check_me = input("press y and [ENTER] to add another campaign budget, or n and [enter] to output ascii graphs: ")
            if check_me.lower() not in self.question:
                print("please select y or n")
            else:
                return check_me
    def printCampaign(sef):
        print("------CAMPAIGN QUERY--------")
        cursors['cursor1'].execute("""
        select * from CAMPAIGN
        """)
        for row in cursors['cursor1'].fetchall():
            print("%s %s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4], row[5]))
    def queryCampaign(self):
        cursors['cursor1'].execute("""
        select * from CAMPAIGN
        """)
        return cursors['cursor1'].fetchall()
    
    def grabCampaignName(self,CID):
        query = """
        select Name from CAMPAIGN
        where CID = %s
        """
        cursors['cursor4'].execute(query,(CID,))
        res = cursors['cursor4'].fetchone()
        cname = res[0] if res else 0
        return cname

    def convertCampaignToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            self.campaigns[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.campaigns
    def run(self):
        campaign_arr = self.campaigns.keys()
        try:
            chooseCID = input("Please choose a corresponding campaign to find accounting information: ")
            chooseCID = int(chooseCID)
        except ValueError:
            print("please make sure you select an integer ")
        if chooseCID in campaign_arr:
            print("this campaign is indeed in the DB")
            return chooseCID
        else:
            print("please select a campaign in the DB")
    def findInflows(self,CID):
        query = """
        select sum(total) as dAmount from DONATES
        where total > 5000 and CID in(select CID from DONATOR where DONATOR.CID = %s);
        """

        cursors['cursor12'].execute(query,(CID,))
        
        res = cursors['cursor12'].fetchone()
        inflows = res[0] if res else 0
        if inflows == None:
            inflows = 0
        #print("the total inflows are", inflows)
        self.money.append(inflows)
    
    def findOutflows(self,CID):
        query = """
        WITH phase_cost as(
        select sum(total) as deficit from EXPENSE2 
        where 
        phaseID in(select phaseID from PHASE where PHASE.CID = %s)),

        event_cost as(
        select sum(total) as deficit from EXPENSE1
        where
        EID in(select EID from EVENT where EVENT.CID = %s)),

        totalDef as (select sum(deficit) as totalDeficit from(select deficit from phase_cost
        union all select deficit from event_cost) as combined)

        select * from totalDef as total_remaining;
        """
        cursors['cursor12'].execute(query,(CID,CID,))
        res = cursors['cursor12'].fetchone()
        outflows = res[0] if res else 0
        if outflows == None:
            outflows = 0
        #print("the total outflows are", outflows)
        self.money.append(outflows)
    
    def budget(self,CID):
        query = """
        select campaignbudget as dAmount from CAMPAIGN where CID = %s;
        """
        cursors['cursor12'].execute(query,(CID,))
        res = cursors['cursor12'].fetchone()
        budget = res[0] if res else 0
        if budget == None:
            budget = 0
        #print("the total budget is", budget)
        self.money.append(budget)
    def ovrBudget(self,CID):
        query = """
        WITH phase_cost as(
        select sum(total) as deficit from EXPENSE2 
        where 
        phaseID in(select phaseID from PHASE where PHASE.CID = %s)),

        event_cost as(
        select sum(total) as deficit from EXPENSE1
        where
        EID in(select EID from EVENT where EVENT.CID = %s)),

        budgetAgg as(
        select sum(total) as dAmount from DONATES
        where total > 5000 and CID in(select CID from DONATOR where DONATOR.CID = %s)),

        totalDef as (select sum(deficit) as totalDeficit from(select deficit from phase_cost
        union all select deficit from event_cost) as combined),

        cBudget as (select campaignbudget as dAmount from CAMPAIGN where CID = %s),

        totalBudget as (select sum(dAmount) as totalB from(select dAmount from budgetAgg union all
        select dAmount from cBudget) as combined)

        select((select * from totalBudget)-(select * from totalDef))as total_remaining;
        """
        cursors['cursor12'].execute(query,(CID,CID,CID,CID,))
        res = cursors['cursor12'].fetchone()
        budget = res[0] if res else self.money[2]
        if budget == None:
            budget = self.money[2]
        #print("the total overbudget is", budget)
        self.money.append(budget)
        return self.money
    
    def asciiBarChart(self,campaignMoney,cidList):       
        labels = ["Inflow-Total","Outflow-Total","Budget-Total","Total-Budget-Remaining"]
        i = 0
        for key, value in campaignMoney.items():
            maxV = max(value)
            print(f"-------{cidList[i]}-------")
            for x in range(0,len(value)):
                barLen = int(value[x]/maxV * 50)
                bar = '$' * barLen
                print(f"{labels[x]} | {value[x]} | {bar}")
            i+=1      


class phaseTwo:
    def __init__(self):
        self.options = {1,2,3,4,5,'x'}
        self.campaigns={}
        self.volunteers = {}
        self.participants = {}
        self.phase = {}
        self.event = {}
        self.question = {'y','n'}

    def display(self):
        print("---------PHASE2---------")
        print("Press 1 and [ENTER] to insert into campaign: ")
        print("Press 2 and [ENTER] to insert into volunteers: ")
        print("Press 3 and [ENTER] to insert into participants: ")
        print("Press 4 and [ENTER] to insert into phase: ")
        print("Press 5 and [ENTER] to insert into events: ")
        print("Press x and [ENTER] to go back to main menu: ")
        p2 = input("press [ENTER] for any of these options: ")
        try:
            if p2.lower() == 'x':
                return 'x'
            if int(p2) in self.options:
                return int(p2)
            else:
                print("please select a number from the list of options")
        except ValueError:
            print("make sure your selection is an integer")
    
    def printCampaign(sef):
        print("------CAMPAIGN QUERY--------")
        cursors['cursor1'].execute("""
        select * from CAMPAIGN
        """)
        for row in cursors['cursor1'].fetchall():
            print("%s %s %s %s %s %s %s" % (row[0],row[1],row[2],row[3],row[4], row[5],row[6]))
    
    def queryCampaign(self):
        cursors['cursor1'].execute("""
        select * from CAMPAIGN
        """)
        return cursors['cursor1'].fetchall()
    def convertCampaignToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            possibleParticipates.append(row[6])
            self.campaigns[row[0]] = possibleParticipates
            possibleParticipates = []
        #print(self.campaigns)
        return self.campaigns
    def insertIntoCampaignTable(self):
        if not self.campaigns:
            max_id = 100
        else:
            max_id = max(self.campaigns.keys())
            max_id = max_id + 1
        campaign_name = input("write the campaign name and press [ENTER]: ")
        campaignBudget = input("Enter a campaign budget and press [ENTER]: ")
        try:
            campaignBudget = float(campaignBudget)
            campaignBudget = round(campaignBudget, 2)
        except ValueError:
            print("Input is an incorrect type")
        print(campaignBudget)
        mission = input("enter a short mission statement: ")
        startDate = input("Enter a start date in YYYY,MM,DD format. Ex: 2022, 04, 13: ")
        startDate = startDate.split(',')
        endDate = input("Enter an end date in YYYY,MM,DD format, that's later than the start date: ") #dates are trickey.
        endDate = endDate.split(',')
        date_arr = checkDate.validateDate(self, startDate, endDate)
        print(date_arr)
        tuple_data = (max_id, campaign_name, campaignBudget, mission, date_arr[0], date_arr[1])
        campaign_data = [tuple_data]
        campsql = "INSERT INTO CAMPAIGN (CID,Name,campaignBudget, mission, startDate, endDate) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            cursors['cursor0'].executemany(campsql, campaign_data)
            dbconn.commit()
            print("campaign inserted successfully")
        except psycopg2.Error as e:
            dbconn.rollback()
            print("there was an error inserting this campaign")
            print(e)
    def campaignQ(self):
        while True:
            check_me = input("press y and [ENTER] create more campaigns, or n and [ENTER] to enter continue: ")
            if check_me.lower() not in self.question:
                print("please select y or n")
            else:
                return check_me

    def queryVolunteer(self):
        cursors['cursor2'].execute("""
        select * from VOLUNTEER
        """)
        return cursors['cursor2'].fetchall()
    def printVolunteer(self):
        print("------VOLUNTEER QUERY--------")
        cursors['cursor2'].execute("""
        select * from VOLUNTEER
        """)
        for row in cursors['cursor2'].fetchall():
            print("%s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4]))
    def convertVolunteerToDict(self,cursor):
        possibleParticipates = []
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            self.volunteers[row[0]] = possibleParticipates
            possibleParticipates = []
        return self.volunteers
    
    def insertIntoVolunteerTable(self):
        if not self.volunteers:
            max_id = 927500
        else:    
            max_id = max(self.volunteers.keys())
            max_id=max_id+1
        volunteerName = input("Please enter a volunteer name: ")
        email = input("Please enter an email: ") #not going to do string parsing for this
        try:
            tierLevel = input("what is the tier level of this volunteer?: ")
            tierLevel = int(tierLevel)
            if tierLevel > 2 or tierLevel < 1:
                print("there are only 2 tier levels to volunteers")
            salary = input("please select a salary where a volunteer has no salary: ")
            salary = int(salary)
        except ValueError:
            print("salaries and tierlevels must be ints")
        if salary <= 0:
            salary = None
        tuple_data = (max_id,volunteerName,email, tierLevel, salary)
        volunteer_data = [tuple_data]
        volsql = "INSERT INTO VOLUNTEER (VID, Name, email, tierLevel, salary) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursors['cursor2'].executemany(volsql,volunteer_data)
            dbconn.commit()
            print("volunteer inserted successfully")
        except psycopg2.Error as e:
            dbconn.rollback()
            print("Error inserting volunteers:", e)
    
    def queryParticipates(self):
        cursors['cursor3'].execute("""
        select * from PARTICIPATES
        """)
        return cursors['cursor3'].fetchall()
    def printParticipates(self):
        print("------PARTICIPANT QUERY--------")
        cursors['cursor3'].execute("""
        select * from PARTICIPATES
        """)
        for row in cursors['cursor3'].fetchall():
            print ("%s %s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4],row[5]))
    def convertParticipatesToDict(self,cursor):
        possibleParticipates=[]
        for row in cursor:
            print ("%s %s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4],row[5]))
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            self.participants[row[0],row[1]] = possibleParticipates
            possibleParticipates = []

        return self.participants
    
    def insertIntoParticipatesTable(self):
        selectedKeys = []
        vol_arr = self.volunteers.keys()
        campaign_arr = self.campaigns.keys()
        print(vol_arr)
        print(campaign_arr)
        try:
            chooseVID = input("Please choose a volunteer to assign to a campaign by selecting their id: ")
            chooseVID = int(chooseVID)
            chooseCID = input("Please choose a corresponding campaign to assign the volunteer: ")
            chooseCID = int(chooseCID)
        except ValueError:
            print("please make sure you select an integer for both")
        if chooseVID in vol_arr:
            print("this volunteer is indeed in the DB")
            selectedKeys.append(chooseVID)
        else:
            print("please select a volunteer in the DB")
        if chooseCID in campaign_arr:
            print("this campaign is indeed in the DB")
            selectedKeys.append(chooseCID)
        else:
            print("please select a campaign in the DB")
        
        print(self.campaigns[chooseCID][3], self.campaigns[chooseCID][4])
        startDate = input("Enter a start date in the array above YYYY,MM,DD format within Ex: 2022, 04, 13: ")
        startDate = startDate.split(',')
        endDate = input("Enter an end date in the array above YYYY,MM,DD format, that's later than the start date: ") #dates are trickey.
        endDate = endDate.split(',')
        date_arr = checkDate.validateDate(self, startDate, endDate)
        dtOrF = checkDate.compareDate(self,date_arr[0],date_arr[1],self.campaigns[chooseCID][3],self.campaigns[chooseCID][4])
        print(dtOrF)
        role = input("what role does this participant play: ")
        if dtOrF == True and len(selectedKeys) == 2:
            tuple_data = (chooseCID, chooseVID, date_arr[0],date_arr[1],role)
            campaign_data = [tuple_data]
            campsql = """
            INSERT INTO PARTICIPATES (CID,VID,startDate,endDate,role)
            VALUES (%s, %s, %s, %s,%s)
            ON CONFLICT (CID, VID) DO NOTHING
            """
            try:
                cursors['cursor6'].executemany(campsql, campaign_data)
                dbconn.commit()
                print("participates inserted successfully")
            except psycopg2.Error as e:
                dbconn.rollback()
                print("there was an error inserting this participant. it may already exist")
                print(e)
    
    def queryPhase(self):
        cursors['cursor3'].execute("""
        select * from PHASE
        """)
        return cursors['cursor3'].fetchall()
    def printPhase(self):
        print("------PHASE QUERY--------")
        cursors['cursor3'].execute("""
        select * from PHASE
        """)
        for row in cursors['cursor3'].fetchall():
            print ("%s %s %s %s %s %s" % (row[0],row[1],row[2],row[3],row[4],row[5]))
    def convertPhaseToDict(self,cursor):
        cursors['cursor3'].execute("""
        select * from PHASE
        """)
        possibleParticipates=[]
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            self.phase[row[0]] = possibleParticipates
            possibleParticipates = []

        return self.phase
    
    def insertIntoPhaseTable(self):
        selectedKeys = []
        if not self.phase:
            max_id = 7000
        else:
            max_id = max(self.phase.keys())
            max_id=max_id+1
        campaign_arr = self.campaigns.keys()
        pushM = input("enter a push method: ")
        try:
            chooseCID = input("Please choose a corresponding campaign to assign the phase: ")
            chooseCID = int(chooseCID)
        except ValueError:
            print("please make sure you select an integer for both")
        if chooseCID in campaign_arr:
            print("this campaign is indeed in the DB")
            selectedKeys.append(chooseCID)
        else:
            print("please select a campaign in the DB")
        
        print(self.campaigns[chooseCID][3], self.campaigns[chooseCID][4])
        startDate = input("Enter a start date in the array above YYYY,MM,DD format within Ex: 2022, 04, 13: ")
        startDate = startDate.split(',')
        endDate = input("Enter an end date in the array above YYYY,MM,DD format, that's later than the start date: ") #dates are trickey.
        endDate = endDate.split(',')
        date_arr = checkDate.validateDate(self, startDate, endDate)
        if date_arr == None:
            print("you did something incorrectly, returning...")
            return
        dtOrF = checkDate.compareDate(self,date_arr[0],date_arr[1],self.campaigns[chooseCID][3],self.campaigns[chooseCID][4])
        print(dtOrF)

        tuple_data = (max_id,pushM,date_arr[0],date_arr[1],chooseCID)
        volunteer_data = [tuple_data]
        volsql = "INSERT INTO PHASE (phaseID, pushMethod, startDate, endDate, CID) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursors['cursor2'].executemany(volsql,volunteer_data)
            dbconn.commit()
            print(" inserted successfully")
        except psycopg2.Error as e:
            dbconn.rollback()
            print("Error inserting volunteers:", e)
    def queryEvent(self):
        cursors['cursor9'].execute("""
        select * from Event
        """)
        return cursors['cursor9'].fetchall()
    def printEvent(self):
        print("------EVENT QUERY--------")
        cursors['cursor9'].execute("""
        select * from EVENT
        """)
        for row in cursors['cursor9'].fetchall():
            print ("%s %s %s %s %s %s " % (row[0],row[1],row[2],row[3],row[4],row[5]))
    def convertEventToDict(self,cursor):
        cursors['cursor9'].execute("""
        select * from EVENT
        """)
        possibleParticipates=[]
        for row in cursor:
            possibleParticipates.append(row[1])
            possibleParticipates.append(row[2])
            possibleParticipates.append(row[3])
            possibleParticipates.append(row[4])
            possibleParticipates.append(row[5])
            self.event[row[0]] = possibleParticipates
            possibleParticipates = []

        return self.event
    
    def insertIntoEventTable(self):
        selectedKeys = []
        if not self.event:
            max_id = 800000
        else:
            max_id = max(self.event.keys())   #if no phase then we have to set a new key for phase, same with all others
            max_id=max_id+1
        campaign_arr = self.campaigns.keys()
        eventName = input("enter an event name: ")
        location = input("enter a location: ")
        try:
            chooseCID = input("Please choose a corresponding campaign to assign the phase: ")
            chooseCID = int(chooseCID)
        except ValueError:
            print("please make sure you select an integer for both")
        if chooseCID in campaign_arr:
            print("this campaign is indeed in the DB")
            selectedKeys.append(chooseCID)
        else:
            print("please select a campaign in the DB")
        
        print(self.campaigns[chooseCID][3], self.campaigns[chooseCID][4])
        startDate = input("Enter a start date in the array above YYYY,MM,DD format within Ex: 2022, 04, 13: ")
        startDate = startDate.split(',')
        date_arr = checkDate.validateDate(self, startDate, startDate)
        if date_arr == None:
            print("you did something incorrectly, returning...")
            return
        dtOrF = checkDate.compareDate(self,date_arr[0],date_arr[1],self.campaigns[chooseCID][3],self.campaigns[chooseCID][4])
        if dtOrF == False:
            print("one of the dates is not in range: ")
            return
        print(dtOrF)

        tuple_data = (max_id,eventName,date_arr[0],location,chooseCID)
        volunteer_data = [tuple_data]
        volsql = "INSERT INTO EVENT (EVID, Name, dDate, Location, CID) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursors['cursor9'].executemany(volsql,volunteer_data)
            dbconn.commit()
            print(" inserted successfully")
        except psycopg2.Error as e:
            dbconn.rollback()
            print("Error inserting volunteers:", e)

class checkDate:
    def __init__(self):
        self.startDate
        self.endDate
    def validateDate(self, startDate, endDate):
        if len(startDate) != 3 or len(endDate) != 3:
            print("length of a date must be equal to 3")
            print(startDate)
            print(endDate)
        try:
            if len((startDate[0])) != 4 or len((startDate[1])) != 2 or len((startDate[2])) != 2:
                print("One of month, day or year is not the right length")
        except Exception as e:
            print("An error has occured:", e)
        try:
            startDate[0] = int(startDate[0])
            startDate[1] = int(startDate[1])
            startDate[2] = int(startDate[2])
            endDate[0] = int(endDate[0])
            endDate[1] = int(endDate[1])
            endDate[2] = int(endDate[2])
        except ValueError:
            print("One of the values is not an integer")
            print(startDate)
            print(endDate)
            return
        try:
            s_compare_date = datetime(startDate[0],startDate[1],startDate[2])
            e_compare_date = datetime(endDate[0],endDate[1],endDate[2])
        except ValueError:
            print("One of the dates don't exist, please try on a different calendar")
            return

        if s_compare_date > e_compare_date:
            print("start date should happen before an end date")
            return
        sqlStartDate = date(startDate[0],startDate[1],startDate[2])
        sqlEndDate = date(endDate[0],endDate[1],endDate[2])

        return [sqlStartDate,sqlEndDate]
    
    def compareDate(self, startDate, endDate, d3, d4):
        print(startDate)
        print(endDate)
        print(d3)
        print(d4)
        if d3 > startDate:
            return False
        if d3 > endDate:
            return False
        if d4 < startDate:
            return False
        if d4 < endDate:
            return False
        return True

class phaseOne:
    def __init__(self):
        self.options ={1,2,3,4,5,6,7,8,9,10,'x'}
        self.question = {"y","n"}
    def display(self):
        print("1) Who are the volunteers that participate in green-love?")
        print("2) What are the campaigns that Clark Davidson is involved in?")
        print("3) Are we over or underbudget for campaign with cid=100?")
        print("4) Who are the 'donators' and what are their emails?")
        print("5) What are the phase costs for all campagins?")
        print("6) How many campaigns happen after Febuary 1st 2024?")
        print("7) What are the earliest and latest start dates for phases?")
        print("8) What are the number of volunteers who participated in campaigns >$2000?")
        print("9) How much total money has been donated to 'Green-Love'?")
        print("10) What is the average salary based on 'employee' tier level\n")
    
    def run(self):
        bool = True
        while bool:
            inpoot = input("Please select a list of queries to execute seperated by commas. ex: 1,3,10 \nyou can also press x then [ENTER] to quit at any time: ")
            inpoot = inpoot.split(',')
            try:
                for x in range(0,len(inpoot)):
                    if inpoot[x].lower() == "x":
                        break
                    elif int(inpoot[x]) not in self.options:
                        print(int(inpoot[x]), "is not in the correct range")
                    else:
                        inpoot[x] = int(inpoot[x])
            except ValueError:
                print(x, "is a non-integer include only integers.")
            
            return inpoot

    def executeQueries(self, inpoot):

        for y in inpoot:
            if y == 1:
                print("\nEXECUTION OF QUERY 1")
                cursors['cursor1'].execute("""
                select CAMPAIGN.Name, VOLUNTEER.Name from CAMPAIGN join PARTICIPATES on CAMPAIGN.CID = PARTICIPATES.CID 
                join VOLUNTEER on VOLUNTEER.VID = PARTICIPATES.VID
                WHERE CAMPAIGN.NAME = 'green-love';
                """)
                for row in cursors['cursor1'].fetchall():
                    print ("%s %s " % (row[0], row[1]))
            elif y == 2:
                print("\nEXECUTION OF QUERY 2")
                cursors['cursor2'].execute("""
                select CAMPAIGN.Name, VOLUNTEER.Name from CAMPAIGN join PARTICIPATES on CAMPAIGN.CID = PARTICIPATES.CID 
                join VOLUNTEER on VOLUNTEER.VID = PARTICIPATES.VID
                WHERE VOLUNTEER.NAME = 'Clark Davidson';
                """)
                for row in cursors['cursor2'].fetchall():
                    print ("%s %s " % (row[0], row[1]))
            elif y == 3:
                print("\nEXECUTION OF QUERY 3")
                cursors['cursor3'].execute("""
                WITH phase_cost as(
                select sum(total) as deficit from EXPENSE2 
                where 
                phaseID in(select phaseID from PHASE where PHASE.CID = 100)),

                event_cost as(
                select sum(total) as deficit from EXPENSE1
                where
                EID in(select EID from EVENT where EVENT.CID = 100)),

                budgetAgg as(
                select sum(total) as dAmount from DONATES
                where total > 5000 and CID in(select CID from DONATOR where DONATOR.CID = 100)),

                totalDef as (select sum(deficit) as totalDeficit from(select deficit from phase_cost
                union all select deficit from event_cost) as combined),

                cBudget as (select campaignbudget as dAmount from CAMPAIGN where CID = 100),

                totalBudget as (select sum(dAmount) as totalB from(select dAmount from budgetAgg union all
                select dAmount from cBudget) as combined)

                select((select * from totalBudget)-(select * from totalDef))as total_remaining;
                """)
                for row in cursors['cursor3'].fetchall():
                    print ("%s " % (row[0]))
            elif y == 4:
                print("\nEXECUTION OF QUERY 4")
                cursors['cursor4'].execute("""
                select Name, email from DONATOR join 
                DONATES on(DONATES.DID = DONATOR.DID) where total >= 5000 and 
                DONATES.CID = 100;
                """)
                for row in cursors['cursor4'].fetchall():
                    print ("%s %s " % (row[0], row[1]))
            elif y == 5:
                print("\nEXECUTION OF QUERY 5")
                cursors['cursor5'].execute("""
                select CID, sum(total) as deficit from EXPENSE2 
                join PHASE on(PHASE.phaseID = EXPENSE2.phaseID) group by CID;
                """)
                for row in cursors['cursor5'].fetchall():
                    print ("%s %s " % (row[0], row[1]))
            elif y == 6: 
                print("\nEXECUTION OF QUERY 6")
                cursors['cursor6'].execute("""
                select CAMPAIGN.Name, PHASE.pushMethod from CAMPAIGN join PHASE on CAMPAIGN.CID = PHASE.CID
                where PHASE.startDate > '2024-02-01';
                """)
                for row in cursors['cursor6'].fetchall():
                    print ("%s %s " % (row[0], row[1]))
            elif y == 7:
                print("\nEXECUTION OF QUERY 7")
                cursors['cursor7'].execute("""
                select CID, min(startDate), max(endDate)
                from PHASE group by CID;
                """)
                for row in cursors['cursor7'].fetchall():
                    print ("%s %s %s " % (row[0], row[1], row[2]))
            elif y == 8:
                print("\nEXECUTION OF QUERY 8")
                cursors['cursor8'].execute("""
                select count(*) from (select VID from PARTICIPATES where CID in
                (select CID from CAMPAIGN where campaignBudget > 2000)) as final;
                """)
                for row in cursors['cursor8'].fetchall():
                    print ("%s " % (row[0]))
            elif y == 9:
                print("\nEXECUTION OF QUERY 9")
                cursors['cursor9'].execute("""
                select sum(total) as total_love_donation
                from donates where CID = (select CID from CAMPAIGN where name = 'green-love');
                """)
                for row in cursors['cursor9'].fetchall():
                    print ("%s " % (row[0]))
            elif y == 10: 
                print("\nEXECUTION OF QUERY 10")
                cursors['cursor10'].execute("""
                select tierLevel, avg(Salary) from VOLUNTEER group by tierLevel;
                """)
                for row in cursors['cursor10'].fetchall():
                    print ("%s %s " % (row[0], row[1]))

    def p1_question(self):
        while True:
            check_me = input("press y and [ENTER] re-run queries, or n and [ENTER] to go back to main-menu: ")
            if check_me.lower() not in self.question:
                print("please select y or n")
            else:
                return check_me

class Menu:
    def __init__(self):
        self.options = {1,2,3,4,5,'x'}
    
    def display(self):
        print("Press 1 and [ENTER] to run queries from A3")
        print("Press 2 and [ENTER] to set up a campaign")
        print("Press 3 and [ENTER] to get some accounting information")
        print("Press 4 and [ENTER] to get membership history")
        print("Press 5 and [ENTER] to insert into donates")
        print("Press x and [ENTER] to exit")
    
    def run(self):
        bool = True
        
        while bool:
            inpoot = input("\nplease select an option from above: ")
            try:
                if inpoot.lower() == "x":
                    break
                elif(int(inpoot) not in self.options):
                    print(int(inpoot), "is not in the correct range \n")
                else:
                    return int(inpoot)
            except ValueError:
                print(inpoot, "is a non-integer include only integers \n")

def main():
    menu = Menu()
    menu.display()
    menu_option = menu.run()
    print(menu_option)
    if(menu_option == 1):
        while True:
            p1 = phaseOne()
            p1.display()
            p1_option = p1.run()
            p1.executeQueries(p1_option)
            cont = p1.p1_question()
            if(cont == 'n'):
                return main()
    elif(menu_option == 2):
        while True:
            p2 = phaseTwo()
            menu2Option = p2.display()
            cont = p2Main(menu2Option,p2)
            if(cont == 'n'):
                return main()
    elif(menu_option == 3):
        campaignMoney = {}
        cidList = []
        while True:
            p3 = phaseThree()
            b = p3.queryCampaign()
            p3.convertCampaignToDict(b)
            p3.printCampaign()
            cid = p3.run()
            p3.findInflows(cid)
            p3.findOutflows(cid)
            p3.budget(cid)
            money = p3.ovrBudget(cid)
            campaignMoney[cid] = money
            cname = p3.grabCampaignName(cid)
            cidList.append(cname)
            cont = p3.p3_question()
            if(cont == 'n'):
                print(campaignMoney)
                p3.asciiBarChart(campaignMoney, cidList)
                return main()
    
    elif(menu_option == 4):
        while True:
            p4 = phaseFour()
            option = p4.display()
            if option == 'x':
                return main()
            if option == 1:
                v = p4.queryVolunteer()
                p4.convertVolunteerToDict(v)
                p4.printVolunteer()
                vid = p4.run()
                print(vid)
                if 'x' in vid:
                    print("exiting")
                else:
                    for x in vid:
                        p4.getMembershipHistory(x)
            
            elif option == 2:
                while True:
                    option2 = p4.display2()
                    if option2 == 'x':
                        break
                    if option2 == 1: #add annotations to 
                        b = p4.queryCampaign()
                        cmd = p4.convertCampaignToDict(b)
                        p4.printCampaign()
                        p4.addCampaignAnnotations(cmd)
                        p4.printCampaign()
                    if option2 == 2: #add annotations to 
                        b = p4.queryPhase()
                        cmd = p4.convertPhaseToDict(b)
                        p4.printPhase()
                        p4.addPhaseAnnotations(cmd)
                        p4.printPhase()
                    if option2 == 3: #add annotations to 
                        b = p4.queryEvent()
                        cmd = p4.convertEventToDict(b)
                        p4.printEvent()
                        p4.addEventAnnotations(cmd)
                        p4.printEvent()
                    if option2 == 4: #add annotations to 
                        b = p4.queryCampaign()
                        cmd = p4.convertCampaignToDict(b)
                        g = p4.queryVolunteer()
                        gmd = p4.convertVolunteerToDict(g)
                        p4.printParticipates()
                        p4.addParticipatesAnnotations(cmd,gmd)
                        p4.printParticipates()
                        



    elif(menu_option == 5):
        while True:
            p5 = phaseFive()
            v = p5.queryCampaign()
            p5.convertCampaignToDict(v)
            p5.printCampaign()
            w = p5.queryDonator()
            p5.convertDonatorToDict(w)
            p5.printDonator()
            p5.insertIntoDonatesTable()
            p5.printDonates()
            cont = p5.p5_question()
            if(cont == 'n'):
                return main()

    for cursor in cursors.values():
        cursor.close()

    dbconn.close()
            

def p2Main(menu2Option,p2):
    print(menu2Option)
    if menu2Option == 1:
        c = p2.queryCampaign()
        p2.convertCampaignToDict(c)
        p2.insertIntoCampaignTable()
        p2.printCampaign()
        cont = p2.campaignQ()
        if(cont == 'n'):
            return 'n'
        else:
            p2Main(1,p2)
    elif menu2Option == 2:
        c= p2.queryCampaign()
        p2.convertCampaignToDict(c)
        v= p2.queryVolunteer()
        p2.convertVolunteerToDict(v)
        p2.insertIntoVolunteerTable()
        p2.printVolunteer()
        cont = p2.campaignQ()
        if(cont == 'n'):
            return 'n'
        else:
            p2Main(2,p2)
    elif menu2Option == 3:
        c= p2.queryCampaign()
        p2.convertCampaignToDict(c)
        p2.printCampaign()
        v= p2.queryVolunteer()
        p2.convertVolunteerToDict(v)
        p2.printVolunteer()
        p2.insertIntoParticipatesTable()
        p2.printParticipates()
        cont = p2.campaignQ()
        if(cont == 'n'):
            return 'n'
        else:
            p2Main(3,p2)
    elif menu2Option == 4:
        c= p2.queryCampaign()
        p2.convertCampaignToDict(c)
        p2.printCampaign()
        p = p2.queryPhase()
        p2.convertPhaseToDict(p)
        p2.insertIntoPhaseTable()
        p2.printPhase()
        cont = p2.campaignQ()
        if(cont == 'n'):
            return 'n'
        else:
            p2Main(4,p2)
    elif menu2Option == 5:
        c= p2.queryCampaign()
        p2.convertCampaignToDict(c)
        p2.printCampaign()
        e = p2.queryEvent()
        p2.convertEventToDict(e)
        p2.insertIntoEventTable()
        p2.printEvent()
        cont = p2.campaignQ()
        if(cont == 'n'):
            return 'n'
        else:
            p2Main(5,p2)
    elif menu2Option == 'x':
        main()


if __name__ == '__main__':
    main()
            
