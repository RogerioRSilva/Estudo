var num1 = prompt('Digite o valor de num1: ')
var num2 = prompt('Digite o valor de num2: ')

num1 = parseInt(num1)
num2 = parseInt(num2)


document.write('A soma entre ' + num1 + ' e ' + num2 + ' é: ' + (num1 + num2) + '<br>')
document.write('A Subtração entre ' + num1 + ' e ' + num2 + ' é: ' + (num1 - num2) + '<br>')
document.write('A Multiplicação entre ' + num1 + ' e ' + num2 + ' é: ' + (num1 * num2) + '<br>')
document.write('A Divisão entre ' + num1 + ' e ' + num2 + ' é: ' + (num1 / num2) + '<br>')
document.write('O modulo entre ' + num1 + ' e ' + num2 + ' é: ' + (num1 % num2) + '<br>')
//Quando colocamos o incremento antes da variável a mesma sofre a modificação no ato  
//de carregar a informação.
document.write('O incremento de ' + num1 + ' é: ' + (++num1) + '<br>')
document.write('O incremento de ' + num1 + ' é: ' + (++num1) + '<br>')
document.write('O incremento de ' + num1 + ' é: ' + (++num1) + '<br>')
//Quando colocamos o incremento após a variável a mesma sofre a modificação após 
//carregar a informação.
document.write('O incremento de ' + num1 + ' é: ' + (num1++) + '<br>')
document.write('O incremento de ' + num1 + ' é: ' + (num1++) + '<br>')
document.write('O incremento de ' + num1 + ' é: ' + (num1++) + '<br>')

document.write('O decremento de ' + num1 + ' é: ' + (--num2) + '<br>')
document.write('O decremento de ' + num1 + ' é: ' + (--num2) + '<br>')
document.write('O decremento de ' + num1 + ' é: ' + (--num2) + '<br>')
document.write('O decremento de ' + num1 + ' é: ' + (num2--) + '<br>')
document.write('O decremento de ' + num1 + ' é: ' + (num2--) + '<br>')
document.write('O decremento de ' + num1 + ' é: ' + (num2--) + '<br>')