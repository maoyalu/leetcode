/* ********** Attempt 1 - 2019/09/21  ********** */

SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId