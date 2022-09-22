var a = prompt('Digite o 1º valor desejado: ')
var b = prompt('Digitte o 2º valor desejado: ')
var c = null

document.write('O primeiro valor digitado foi: ' + a + '<br>')
document.write('O segundo valor digitado foi: ' + b)
document.write('<hr>')
document.write('<br>')

c = a
a = b
b = c

console.log('Variavel A = ' + a)
console.log('Variavel B = ' + b)
console.log('Variavel C = ' + c)


document.write('<h2>O 1º numero digitado foi: ' + a +'</h2><br>')
document.write('<h2>O 2º numero digitado foi: ' + b + '</h2>')
