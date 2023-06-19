SELECT * FROM person.Person

SELECT Title FROM person.person


SELECT FirstName, LastName
FROM person.Person


--Faz o filtro sem repetição somente dados únicos. 
SELECT DISTINCT FirstName 
FROM Person.person

SELECT DISTINCT LastName
FROM Person.person

-- Seleção específica utilizando o where
SELECT *
FROM person.person
WHERE LastName = 'miller'

SELECT *
FROM person.person
WHERE LastName = 'miller' and FirstName = 'anna'

SELECT *
FROM production.Product
Where color = 'blue' or color = 'black'

SELECT *
FROM Production.Product
Where ListPrice > 1500

SELECT Name
FROM Production.Product
Where weight > 500 and weight < 700


SELECT *
FROM HumanResources.Employee
Where MaritalStatus = 'M' and SalariedFlag = 1

SELECT *
FROM person.Person
Where FirstName = 'Peter' AND LastName = 'Krebs'

SELECT EmailAddress
FROM person.EmailAddress
Where BusinessEntityID = 26

--Utilizando o count para fazer contagem de linhas. 
SELECT count(Title)
FROM person.Person

SELECT count(*)
FROM Production.Product

SELECT count(size)
FROM Production.Product

SELECT COUNT(DISTINCT size)
FROM Production.Product

-- Utilizando o ORDER BY e TOP
SELECT TOP 10 *
FROM Production.Product


SELECT *
FROM Person.Person
ORDER BY FirstName desc


SELECT TOP 10 ProductID
FROM Production.Product
ORDER BY ListPrice desc


SELECT TOP 4 Name, ProductNumber
FROM Production.Product
ORDER BY ProductID asc