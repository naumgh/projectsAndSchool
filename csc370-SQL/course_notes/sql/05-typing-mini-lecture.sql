-- CSC 370, Spring 2024
--
-- Notes for mini-lecture of March 14, 2024 (Thursday)
--
-- Topics:
-- * char, varchar, text
-- * ints, floats, numerics
-- * booleans
-- * date

-- Goal is *not* to explain the ins and outs of data types in the
-- Postgres universe. It is too large, and the SQL standard history is
-- too convoluted.
--
-- Rather it is to show types that may be immediately of interest, as
-- well as SQL commands that use the types, along with operations on
-- those types.


-- #######################
-- String types
--

drop table uvic_units cascade;
create table uvic_units (
    name    varchar(40),
    kind    char(10),
    code    char(4),
    blurb   text
);

insert into uvic_units(name, kind, code, blurb)
    values('Computer Science', 'department', 'COSI',
'The Computer Science department was formed in 1980 when
four members of the Math & Stats department created a
committee to investigate the possibility of its creation.
It became part of the Faculty of Engineering upon creation
of that faculty in 1982.');

insert into uvic_units
    values('Civil Engineering', 'department', 'CIVE',
'As of 2024, newest department in the faculty of engineering');

insert into uvic_units
    values('Engineering', 'faculty', 'ENGR',
'Formed in 1982');

insert into uvic_units
    values('Co-op Japan', 'admin', 'COJA',
'Connects Canadian engineering and science undergraduate students
with Japanese businesses. Imagine the food you can experience if
you were on such a co-op!');

insert into uvic_units
    values('Music', 'school', 'MUSI',
'Instructor''s wife studied there from 1986 to 1990 and received
a BMus. She''s really smart.');

insert into uvic_units
    values('Residence and University Food Services', 'admin', 'HFCS',
'Complain about food on campus to these folks, please');


select code, name, kind from uvic_units order by code;

select name, code from uvic_units where kind = 'department';


-- The tilde operator (~) seen below is taken from Perl, equivalent
-- to "<string to search> ~ <regular expression>" where the result
-- of the operation is true or false.
---


select name from uvic_units where blurb ~ '^.*food.*$';

-- This won't success as the four value is a string longer than
-- four characters, and this value her is being provided for an
-- attribute that has a fixed with of four (4) characters.
---

insert into uvic_units
    values('Piracy', 'school', 'ARRRRR', 'Ahoy matey.');



-- #######################
-- Number types
--

drop table workshops cascade;
create table workshops(
    name       varchar(30),
    num_enroll integer, -- same as `int4` or `int`
    weight     float, -- same as `float4`
    price      numeric(6,2)
);

insert into workshops(name, num_enroll, weight, price)
values ('Better Living with Sponges', 3, 450, 35.00);

-- Numeric types specify two parameters -- the "precision"
-- and the "scale"; the former is the total number of permitted
-- digits, and the latter is the number of digits permitted
-- in the fractional part. 

-- If more digits are provided in the fractional part than are
-- permitted, PostgreSQL will round up or down appropriately.
--

insert into workshops
values ('IoT and Apple Juice', 10, 1430.9, 45.505);

insert into workshops
values ('How to Shred a Laptop', 0, 0, 95.101);

\echo select * from workshops;
select * from workshops;


-- If more digits are provided than can be represented by the
-- total number of digits, even with rounding, then any
-- associated insert will fail.
--

-- Will FAIL
insert into workshops 
    values ('Herding Cats with ChatGPT', 12, 1900, 100000);

-- Will SUCCEED
insert into workshops 
    values ('Inner Peace with Haagen Dazs', 100, 18000, 9999.99);

-- Will FAIL
insert into workshops 
    values ('Inner Peace with Haagen Dazs', 100, 18000, 9999.995);

select * from workshops;


-- PostgreSQL also offers an useful "sequence" number type which is
-- normally used to create a sequence of digits than can become
-- unique identifiers.  The "sequence" is a schema object (like a 
-- table), and PostgreSQL permits a shortcut where we can use the
-- "serial" type for an attribute to both create a sequence (if it
-- doesn't already exist) and to cause it to increase in value as it
-- used.i
--

drop table people_who_live_in_wales cascade;
create table people_who_live_in_wales(
    id       serial,
    name     varchar(20)
);

insert into people_who_live_in_wales(name) values ('Jones');
insert into people_who_live_in_wales(name) values ('Jones');
insert into people_who_live_in_wales(name) values ('Jones');
insert into people_who_live_in_wales(name) values ('Davies');
insert into people_who_live_in_wales(name) values ('Jones');
insert into people_who_live_in_wales(name) values ('Jones');
insert into people_who_live_in_wales(name) values ('Davies');

select * from people_who_live_in_wales;


-- #######################
-- Boolean types
--

drop table will_it_float cascade;
create table will_it_float(
    name_of_thing  varchar(30),
    it_floats      boolean
);

insert into will_it_float(name_of_thing, it_floats)
values('sponge', true);

insert into will_it_float values('rock', false);


-- There are many different synonyms for true and false.
-- These are shown below, and should not be mysterious. 
-- Ultimately, however, they are stored in a boolean attribute
-- as t or f values.
--

insert into will_it_float values ('coin', '0');
insert into will_it_float values ('pizza slice', '1');
insert into will_it_float values ('basketball', 'yes');
insert into will_it_float values ('bowling ball', 'no');


-- Like everywhere else in SQL, it is possible for a
-- boolean value to be given a null value.
--

insert into will_it_float(name_of_thing) values ('witch');
select * from will_it_float;


-- One pleasant thing about the syntax involving booleans is that
-- simple referring to the boolean attribute in a "where" clause
-- will use it's true or false value directly in the expression.
--

select * from will_it_float where it_floats;


-- There also exist bitfield / bitvector types (more precisely,
-- "bitstring" types). You can read more about them at:
-- https://www.postgresql.org/docs/current/datatype-bit.html


-- #######################
-- Date types
--

-- These types are perhaps the most confusing because there are
-- dates, times, timestamps, date + time combinations, times
-- with timezones, times without timeszones, etc. 
-- 
-- For chapter and verse, have a look at:
--   https://www.postgresql.org/docs/current/functions-datetime.html
--
-- Here we will narrowly focus on the `date` type plus a few
-- useful operations on dates.
--

drop table important_dates cascade;
create table important_dates (
    course    varchar(20),
    event     varchar(20),
    occurs    date
);


-- There are a few different ways to indicate a particular date.
-- Some are shown here.
--

insert into important_dates(course, event, occurs)
    values('CSC 370', 'final exam', '2024-04-20');

insert into important_dates
    values('CSC 370', 'last lecture', '20240408');

insert into important_dates
    values('CSC 360', 'final exam', 'April 16, 2024');

insert into important_dates
    values('CSC 360', 'last lecture', date '2024-04-05');

insert into important_dates
    values('CSC 360', 'assignment 3 due', '2024-03-22');

insert into important_dates
    values('CSC 370', 'assignment 3 due', '2024-03-18');


select * from important_dates;


-- The kind of error checking you might expect with dates
-- is present here. For example, below are two invalid dates --
-- one clearly invalid, and one which could be a honest
-- error.

insert into important_dates
    values('CSC 666', 'assignment 51 due', '2024-02-30');

insert into important_dates
    values('CSC 666', 'assignment 38 due', '2023-02-29');


-- The calendar order of dates is as you would expect
--

select * from important_dates order by occurs;


-- The meaning of relational operations is also sensible in that
-- "<" means "strictly before", ">=" means "on or after", etc. etc.
--

select * from important_dates order by occurs >= '2024-04-08';


-- There are some built-in values in PostgreSQL, and these are
-- far too large in number to properly cover. However, here is
-- one that is handy.
--

select current_date;


-- This value can actually be used for some useful queries. For 
-- example, we can construct a query which reports the number of days
-- from the today (current date) until the important dates in the
-- table.
--

select occurs - current_date as days_away, course, event
from important_dates;

select occurs - current_date as days_away, course, event
from important_dates
order by days_away;


-- FYI: Some other handy values that can be directly obtained
-- using `select`.
--
-- Notice how some look like variables, and some look like
-- functions.
--

select current_time;
select current_timestamp;  -- Beware Year 2037 problem...
select localtime;
select now();
select extract(century from timestamp '2024-03-14 10:00:00');
select extract(doy from timestamp '2024-03-14 10:00:00');


-- Do not become to mesmerized by these date and time stamps.
-- Use the minimum of what is needed; anything else could lead
-- you into a swamp of bugs.
--
