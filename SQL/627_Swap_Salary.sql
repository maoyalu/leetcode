/* ********** Attempt 1 - 2019/09/20  ********** */

UPDATE salary
SET sex = CASE
WHEN sex = 'm' THEN 'f'
WHEN sex = 'f' THEN 'm'
END
WHERE sex IN ('m', 'f');