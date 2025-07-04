--location table
create table location(
	id serial primary key,
	city varchar(255) NOT NULL,
	--not every country uses states, but provinces, oblasks, etc are all functioanlyl equivalent
	state varchar(255) NOT NULL,
	country varchar(255) NOT NULL
);

--person table, 1 to many with location
create table person(
	id serial primary key,
	firstName varchar(50) NOT NULL,
	lastName varchar(50) NOT NULL,
	age smallint,
	location_id INTEGER REFERENCES location(id)
	
);

--person_interest table, many to one with person
--really, this is just a many-to-many iwth interest

create table interest(
	id serial primary key,
	title varchar(255) NOT NULL
);

create table person_interest(
	person_id INTEGER NOT NULL REFERENCES person(id),
	interest_id INTEGER NOT NULL REFERENCES interest(id),
	primary key (person_id, interest_id)
);

--HERE WE CAN BEGIN INSERTIONS
--insert location first
insert into location (city, state, country) 
values
	('Nashville', 'Tennessee', 'United States'),
	('Memphis', 'Tennessee', 'United States'),
	('Phoenix', 'Arizona', 'United States'),
	('Denver', 'Colorado', 'United States');
--insert person next
insert into person (firstName, lastName, age, location_id) 
values
	('Chickie', 'Ourtic', 21, 1),
	('Hilton', 'O’Hanley', 37, 1),
	('Barbe', 'Purver', 50, 3),
	('Reeta', 'Sammons', 34, 2),
	('Abbott', 'Fisbburne', 49, 1),
	('Winnie', 'Whines', 19, 4),
	('Samantha', 'Leese', 35, 2),
	('Edouard', 'Lorimer', 29, 1),
	('Mattheus', 'Shaplin', 27, 3),
	('Donnell', 'Corney', 25, 3),
	('Wallis', 'Kauschke', 28, 3),
	('Melva', 'Lanham', 20, 2),
	('Amelina', 'McNirlan', 22, 4),
	('Courtney', 'Holley', 22, 1),
	('Sigismond', 'Vala', 21, 4),
	('Jacquelynn', 'Halfacre', 24, 2),
	('Alanna', 'Spino', 25, 3),
	('Isa', 'Slight', 32, 1),
	('Kakalina', 'Renne', 26, 3);

insert into interest (title)
values
	('Programming'),
	('Gaming'),
	('Computers'),
	('Music'),
	('Movies'),
	('Cooking '),
	('Sports');
	
insert into person_interest (person_id, interest_id)
values
	(1, 1),(1, 2),(1, 6),(2, 1),(2, 7),(2, 4),(3, 1),
	(3, 3),(3, 4),(4, 1),(4, 2),(4, 7),(5, 6),(5, 3),
	(5, 4),(6, 2),(6, 7),(7, 1),(7, 3),(8, 2),(8, 4),
	(9, 5),(9, 6),(10, 7),(10, 5),(11, 1),(11, 2),(11, 5),
	(12, 1),(12, 4),(12, 5),(13, 2),(13, 3),(13, 7),(14, 2),
	(14, 4),(14, 6),(15, 1),(15, 5),(15, 7),(16, 2),(16, 3),
	(16, 4),(17, 1),(17, 3),(17, 5),(17, 7),(18, 2),(18, 4),
	(18, 6),(19, 1),(19, 2),(19, 3),(19, 4),(19, 5),
	(19, 6),(19, 7);

--UPDATE USER AGE (ADDING 1 TO CURRENT AGE)
update person set age = age + 1 where (firstName, lastName) in (
  ('Chickie',   'Ourtic'),
  ('Winnie',    'Whines'),
  ('Edouard',   'Lorimer'),
  ('Courtney',  'Holley'),
  ('Melva',     'Lanham'),
  ('Isa',       'Slight'),
  ('Abbott',    'Fisbburne'),
  ('Reeta',     'Sammons')
);

--deletion of persons
delete from person_interest
where person_id in(
	select id from person where(firstName, lastName) in(
	('Hilton','O’Hanley'),('Alanna','Spino'))
);

delete from person
where id in(
	select id from person where(firstName, lastName) in(
	('Hilton','O’Hanley'),('Alanna','Spino'))
);



--additional sql select statements
select * from interest;


--get names
SELECT firstName, lastName from person;

--find all people who live in Nashville, TN
SELECT firstName, lastName, l.city, l.state from PERSON as p
join location as l 
on p.location_id = l.id
where l.city = 'Nashville' and l.state = 'Tennessee' and l.country = 'United States';

--how many people live in each of our four cities
SELECT l.city, count(*) from PERSON as p join location as l 
on(p.location_id = l.id) group by l.city;

--how many people are interested in each of the 7 interests
Select i.title, count(*) from interest as i join person_interest as pi
on(i.id = pi.person_id) group by i.title;

--finds the names (first and last) of all the people who live in Nashville, TN 
--and are interested in programming

with nashville_table as(
SELECT p.id as person_id, p.firstName, p.lastName, l.city, l.state from PERSON as p
join location as l 
on p.location_id = l.id
where l.city = 'Nashville' and l.state = 'Tennessee' and l.country = 'United States')
SELECT nt.firstName, nt.lastName, nt.city, nt.state, i.title from interest as i join person_interest 
as pi on i.id = pi.interest_id join nashville_table as nt on nt.person_id = pi.person_id where i.title = 'Programming';

--using unions, determine how maany people in each age range
SELECT '20–30' AS range, COUNT(*) AS cnt
FROM person
WHERE age >= 20 and age <= 30
union all
SELECT '31-40' as range, count(*) as cnt
from person where age >= 31 and age <= 40
union all
select '41-50' as range, count(*) as cnt
from person where age >= 41 and age <= 50;