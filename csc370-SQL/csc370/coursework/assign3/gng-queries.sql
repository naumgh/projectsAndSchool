--Who are the volunteers that participate in green-love? (1)
select CAMPAIGN.Name, VOLUNTEER.Name from CAMPAIGN join PARTICIPATES on CAMPAIGN.CID = PARTICIPATES.CID 
join VOLUNTEER on VOLUNTEER.VID = PARTICIPATES.VID
WHERE CAMPAIGN.NAME = 'green-love';
--what are the campaigns that Clark Davidson is involved in? (2)
select CAMPAIGN.Name, VOLUNTEER.Name from CAMPAIGN join PARTICIPATES on CAMPAIGN.CID = PARTICIPATES.CID 
join VOLUNTEER on VOLUNTEER.VID = PARTICIPATES.VID
WHERE VOLUNTEER.NAME = 'Clark Davidson';
--we can post a question involving many queries. Specifically, is green-love over budget?

--are we over or underbudget for campaign with cid=100? (3)
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

---select * from totalBudget;
--select * from totalDef;
--select * from cBudget;
--select * from budgetAgg;

select((select * from totalBudget)-(select * from totalDef))as total_remaining;

--so for the green-love campaign, we are approximately $3695.77 overbudget.

--who are the 'donators' and what are their emails? (4)
select Name, email from DONATOR join DONATES on(DONATES.DID = DONATOR.DID) where total >= 5000 and DONATES.CID = 100;
--tim cook and bill gates are two people who could be considered 'donators' for campaign with cid = 100

--let's do a more succint query what are the phase costs for all campagins? (5)
select CID, sum(total) as deficit from EXPENSE2 
join PHASE on(PHASE.phaseID = EXPENSE2.phaseID) group by CID;

--how many campaigns happen after Febuary 1st 2024? (6)
select CAMPAIGN.Name, PHASE.pushMethod from CAMPAIGN join PHASE on CAMPAIGN.CID = PHASE.CID
where PHASE.startDate > '2024-02-01';

--what are the earliest and latest start dates for phases? (7)
select CID, min(startDate), max(endDate)
from PHASE group by CID;

--what are the number of volunteers who participated in campaigns >$2000? (this includes "Employees")(8)
select count(*) from (select VID from PARTICIPATES where CID in
(select CID from CAMPAIGN where campaignBudget > 2000)) as final;

--how much total money has been donated to 'Green-Love'? (9)
select sum(total) as total_love_donation from donates where CID = (select CID from CAMPAIGN where name = 'green-love');

--what is the average salary based on 'volunteer' tier level? (10)
select tierLevel, avg(Salary) from VOLUNTEER group by tierLevel;
--looks like their-level for 1 is null because no one is paid anything for tier-level 1



