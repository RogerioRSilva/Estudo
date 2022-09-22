var nome = 'Maria'
var idade = 27

var nome2 = prompt('Digite o seu nome: ')

var idade2 = prompt('Digite a sua idade: ')

//Exibição dos dados no console do navegador
console.log(nome)
console.log(idade)
console.log(nome2)
console.log(idade2)

//A concatenação é utilizada com o sinal de operação + 
//jundo com uma variável 
document.write('<h1>Olá ' + nome + ' , tudo bem?</h1>')

document.write('<p>Estou vendo que vc possui ' + idade + ' anos.</p>')

document.write('<h2>Olá ' + nome2 + ', Tudo bem? O Sr(a) tem ' + idade2 + ' anos de idade. </h2>')

