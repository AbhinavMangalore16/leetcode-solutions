-- Last updated: 3/31/2026, 9:39:11 PM
# Write your MySQL query statement below
select firstName, lastName, city, state from Person left join Address on Person.personId = Address.personId;