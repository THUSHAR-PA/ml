# String Functions
 LENGTH('sky') - 3 

 SELECT first_name,LENGTH(first_name)
 FROM employee_demographics
 ORDER BY 2;


UPPER('sky') -> SKY 
LOWER('SKY") -> sky

eg: SELECT first_name,UPPER(first_name)
FROM employee_demographics 

TRIM() - trims teh white space both the leading and  trailing
LTRIM() - removes teh leading white space
RTRIM() - removes the trailing white space 


LEFT(string , length) -> finds teh substring and provides the substring with length from its left side

RIGHT(s,len) - >. same as left but right

SUBSTRING(string, pos , how many character to go from that position)

SUBSTRING(birth_date,6,2) - > will provide the month 

REPLACE(string, specify waht to replace, with what to replace)

LOCATE('thing to locate' , string)

CONCAT(s1,s2) - > concatinate two columns
