/* <<<<<<<<<<<<<<< OPERADORES RELACIONAIS >>>>>>>>>>>>>>>>>
Os oepradores relacionais sempre vão retornar valores boleanos
como TRUE e FALSE
    > = Maior
    < = Menor
    >= = Maior Igual
    <= = Menor Igual
    == = Igual
    != = Diferente

    Identicos são utilizados para diferenciar os tipos de variáveis
    usando o sinal: 
    === que é identitico tanto conteúdo quanto o tipo
    !== que é difernete tanto no conteúdo quanto no tipo 

    Os operadores lógicos são utilizados para tomadas de decisão:
    ! = Negação
    && = Conjunção (e)
    ||  = Disjunção (ou)

*/

var maior = 5 > 2
var menor = 7 < 4
var maior_igual = 8 >= 8
var menor_igual = 9<= 7
var igual = 5 == 5
var dif = 4 != 4

console.log(`5 é maior que 2: ${maior}`)
console.log(`7 é menor que 4: ${menor}`)
console.log(`8 é maior ou igual a 8: ${maior_igual}`)
console.log(`9 é menor ou igual a 7: ${menor_igual}`)
console.log(`5 é igual a 5: ${igual}`)
console.log(`4 é diferente de 4 : ${dif}`)

var a = 5
var b = 8

console.log(`Conjunção 5 menor que 8 e 8 % 2 é igual a 0: ${a > b && b % 2 == 0} `)
console.log(`Disjunção 5 menor igual a 8 ou 8 / 2 é igual a 2: ${a <= b || b/2 == 2} `)

/* Operadores ternários 

É utilizado para simplificar testes lógicos com uma unica informação

? :  = TESTE ? TRUE : FALSE
media >= 7.0 ? "Aprovado":"Reprovado"

*/

var media = 5.5

console.log(media > 7? 'Aprovado':'Reprovado')

media += 3

console.log(media > 7? 'Aprovado':'Reprovado')

var x = 3

var res = x % 2 == 0 ? 5 : 9

console.log(res)

var idade = 30

var r = idade <= 30 ? 'Menor ou igual 30':'Maior que 30'

console.log(r)