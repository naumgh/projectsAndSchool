[BEFORE ISA AND RELATION COMBINATION..]

CAMPAIGN(CID, startDate, endDate, Name, Location, missionStatement, budget)
DONATES(Total)
PHASE(PhaseID, pushMethod, endDate, startDate)
EVENT(EVID, Name, Date, Location)
EXPENSE1(EID, Name, Total, Date)
EXPENSE2(EID2, Name, Total, Date)
PARTICIPATES(startDate, endDate, Role)
VOLUNTEER(VID, Name, Email, tierLevel)
EMPLOYEE(Salary)
DONATES(Total)
DONATOR(DID, Date, Name, Email)
SUPPORTER()
PUSHES()
P_Cost()
E_Cost()

[AFTER ISA AND RELATION COMBINATION.. [] DENOTES KEY CREATED]

CAMPAIGN([CID], Location, Budget, Mission, startDate, endDate]
PHASE([PhaseID], pushMethod, startDate, endDate, CID(fk))      //grabs foreign key from campaign (many-to-one)
EXPENSE1([EID], Name, Date, Total , EVID(fk))	//grabs foreign key from phase (many-to-one)
VOLUNTEER([VID], Name, Email, tier) 
PARTICIPATES([CID(fk),VID(fk)], startDate, endDate, Role) //combines foreign keys from campaign and volunteer
EVENT([EVID], Name, Date, Location, CID(fk)) //grabs fk from campaign
EXPENSE2([EID2], Name, Date, Total, EVID(fk)) //grabs fk from event
DONATES([CID(fk),DID(fk)], Total)  //grabs fks from donator and campaign
DONATOR([DID], Name, Email, Date, CID(fk)) //grabs fk from campaign

Only PARTICIPATES AND DONATES for the relationships remains because they were from a many-to-many relationships. all of the many-one relationships were deleted and NOT turned into tables.

I used NULL method for both employee and supporter ISAs because supporter has no attributes, and salary can easily be determined.




