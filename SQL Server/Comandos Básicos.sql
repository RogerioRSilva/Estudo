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


--Utilizando o BETWEEN

SELECT *
FROM Production.Product
WHERE ListPrice BETWEEN 1000 AND 1500

SELECT *
FROM Production.Product
WHERE ListPrice NOT BETWEEN 1000 AND 1500 --Negativa da busca


--Utilizando o IN 

SELECT *
FROM Person.Person
WHERE BusinessEntityID IN (2,7,13)


SELECT *
FROM Person.Person
WHERE BusinessEntityID NOT IN (2,7,13) -- NEGATIVA



--Utilizando o LIKE

SELECT  *
FROM Person.Person
WHERE FirstName LIKE 'ovi%'

SELECT *
FROM Person.Person
WHERE FirstName LIKE '%to'

SELECT *
FROM Person.Person
WHERE FirstName LIKE '% %' 

SELECT *
FROM Person.Person
WHERE FirstName LIKE '%essa%'

SELECT *
FROM Person.Person
WHERE FirstName LIKE '%ro_' -- Trás apenas um caracter após o 'ro'


-- ============================== DESAFIOS ==============================================

-- 1 - Quantos produtos temos cadastrados no sistema que custam mais que 1500 dolares?

SELECT COUNT(*)
FROM Production.Product
WHERE ListPrice > 1500

-- 2 - Quantas pessoas temos com o sobrenome que inicia com a letra P?

SELECT COUNT(*) as 'Qtd Pessoas com P'
FROM Person.Person
WHERE LastName LIKE 'p%'

-- 3 - Em quantas cidades únicas estão cadastrados nossos clientes?

SELECT COUNT(Distinct(City)) as 'Cidades Cadastradas'
FROM Person.address


-- 4 - Quais as unicas cidades que temos cadastradas em nosso sistema?

SELECT DISTINCT City
FROM Person.Address


-- 5 - Quantos produtos vermelhos tem preço entre 500 a 1000 dolares?

SELECT count(*)
FROM Production.Product
WHERE ListPrice between 500 and 1000 
AND color = 'red'

-- 6 - Quantos produtos cadastrados tem a palavra 'road' no nome deles?

Select count(*)
FROM Production.Product
WHERE Name like '%road%'


--===================================== FIM ============================================================



-- SUM / MIN / MAX / AVG

-- SUM
SELECT TOP 10 sum(linetotal) as 'Total Geral'
FROM SALES.SalesOrderDetail

-- MIN
SELECT TOP 10 MIN(linetotal) as 'Menor Valor'
FROM SALES.SalesOrderDetail

-- MAX
SELECT TOP 10 MAX(linetotal) as 'Maior Valor'
FROM SALES.SalesOrderDetail

--AVG
SELECT TOP 10 AVG(linetotal) as 'Média VAlor'
FROM SALES.SalesOrderDetail



-- =========== UTILIZANDO O GROUP BY ===========

SELECT SpecialOfferID, SUM(UnitPrice) -- Soma todos os valores definidos por ID
FROM Sales.SalesOrderDetail
GROUP BY SpecialOfferID -- Agrupa tudo por ID já somado; 


SELECT ProductId, COUNT(ProductId) 
FROM Sales.SalesOrderDetail
GROUP BY ProductID


SELECT FirstName, COUNT(FirstName)
FROM Person.Person
GROUP BY FirstName

SELECT color, AVG(ListPrice)
FROM Production.Product
Where color = 'silver'
GROUP BY color



-- ===================== DESAFIO ==================================

-- 1 - Quantas pessoas tem o mesmo MiddleNamee agrupadas por MiddleName?

SELECT Middlename, COUNT(FirstName) as 'Qtd Pessoas'
FROM Person.Person
GROUP BY MiddleName


-- 2 - Qual a quantidade média de cada produto vendido na loja?

SELECT ProductID, AVG(OrderQty) as 'Media Vendas p/ Produto'
FROM Sales.SalesOrderDetail
GROUP BY ProductID


-- 3 - Quais foram as 10 vendas que no total tiveram os maiores valores de venda por produto do maior para o menos. 

SELECT TOP 10 ProductID, SUM(linetotal) as 'Total Vendido'
FROM Sales.SalesOrderDetail
GROUP BY ProductID
ORDER BY SUM(LineTotal) DESC

-- 4 - Quantos produtos e qual a quantidade media de produtos temos cadastrados nas nossas ordem de serviços (WorkOrder), agrupados por ProductID

SELECT productId, COUNT(ProductID) as 'SomaProdutos', AVG(OrderQty) as 'Quantidade Média Produtos' 
FROM Production.WorkOrder
GROUP BY ProductID 
 
