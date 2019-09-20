/* ********** Attempt 1 - 2019/09/21  ********** */

SELECT E.Name AS Employee
FROM Employee E, Employee M
WHERE E.Salary > M.Salary AND E.ManagerId = M.Id