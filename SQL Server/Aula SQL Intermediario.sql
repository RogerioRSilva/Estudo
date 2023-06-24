use AdventureWorks2017


-- Queremos saber quais nomes no sistema tem um ocorrencia maior que 10 vezes. 

-- utilizando o Having
SELECT FirstName, COUNT(FirstName) as 'Quantidade'
FROM Person.Person
Group BY FirstName
HAVING COUNT(firstname) > 10


SELECT TOP 10 *
FROM Sales.SalesOrderDetail

SELECT ProductID, SUM(linetotal) as 'total'
FROM Sales.SalesOrderDetail
GROUP BY ProductID
HAVING SUM(linetotal) between 16200 and 500000


SELECT FirstName, COUNT(FirstName) 'quantidade'
FROM Person.Person
WHERE Title = 'Mr.'
GROUP BY FirstName
HAVING COUNT(FirstName) > 10

-- ==================================== DESAFIO ===================================

-- 1 - Identificar as provincias(stateProvinceID) com o maior numero de cadastros no nosso sistema,
--     então é preciso encontrar quais provincias (stateProvinceID) estão registradas no BD mais que 1000 vezes.

SELECT stateProvinceID, COUNT(stateProvinceID) as 'Quantidade'
FROM Person.Address
GROUP BY StateProvinceID
HAVING COUNT (StateProvinceID) > 1000


-- 2 - Os gerentes querem saber quais produtos (productID) não estão trazendo em média no mínimo 1 milhão de vendas em total de vendas (linetotal)


SELECT productID, COUNT(linetotal) as 'Total Vendas'
FROM Sales.SalesOrderDetail
GROUP BY ProductID
HAVING AVG(linetotal) < 1000000


-- ================================ INNER JOIN ============================

SELECT TOP 10 *
FROM Person.Person

SELECT TOP 10 *
FROM Person.EmailAddress

SELECT P.BusinessEntityID, P.FirstName, P.LastName, PE.EmailAddress
FROM Person.Person as P
INNER JOIN Person.EmailAddress PE 
ON P.BusinessEntityID = PE.BusinessEntityID


-- Quais os nomes dos produtos e as informações de suas subcategorias

SELECT TOP 10*
FROM Production.Product

SELECT TOP 10 *
FROM Production.ProductSubcategory


SELECT P.ProductSubcategoryID, P.Name, P.ListPrice, ps.Name
FROM Production.Product as P
INNER JOIN Production.ProductSubcategory as ps
ON P.ProductSubcategoryID = ps.ProductSubcategoryID


SELECT *
FROM Production.Product as P
INNER JOIN Production.ProductSubcategory as ps
ON P.ProductSubcategoryID = ps.ProductSubcategoryID


SELECT *
FROM Person.PersonPhone

SELECT *
FROM Person.PhoneNumberType

SELECT PP.BusinessEntityID, PN.Name, PP.PhoneNumberTypeID, PP.PhoneNumber
FROM Person.PersonPhone as PP
INNER JOIN Person.PhoneNumberType as PN
ON PN.PhoneNumberTypeID = PP.PhoneNumberTypeID


SELECT *
FROM Person.Address

SELECT *
FROM Person.StateProvince

SELECT PA.AddressID, PA.City, SP.StateProvinceID, SP.Name
FROM Person.Address as PA
INNER JOIN Person.StateProvince as SP
ON PA.StateProvinceID = SP.StateProvinceID


-- Quero descobrir quais as pessoas não tem um cartão de crédito registrado. 

SELECT *
FROM Person.Person PP
LEFT JOIN Sales.PersonCreditCard PC
ON PP.BusinessEntityID = PC.BusinessEntityID
WHERE PC.BusinessEntityID IS NULL



-- Utilizando o UNION

SELECT [productID], [Name], [ProductNumber]
FROM Production.Product
WHERE Name like '%Chain%'
UNION
SELECT [productID], [Name], [ProductNumber]
FROM Production.Product
WHERE Name like '%Decal%'


-- Utilizando o DatePart 
-- Informações adicionais sobre datepart  https://learn.microsoft.com/en-us/sql/t-sql/functions/datepart-transact-sql?view=sql-server-ver16

SELECT *
FROM Sales.SalesOrderHeader

SELECT SalesOrderID, DATEPART(MONTH,OrderDate) as Mes
FROM Sales.SalesOrderHeader


SELECT AVG(TotalDue) as Media, DATEPART (YEAR,OrderDate) as Ano
FROM Sales.SalesOrderHeader
GROUP BY DATEPART(YEAR, OrderDate)
ORDER BY Ano


SELECT AVG(TotalDue) as Media, DATEPART (Month, OrderDate) as Mes
FROM Sales.SalesOrderHeader
GROUP BY DATEPART(Month, OrderDate)
ORDER BY Mes
