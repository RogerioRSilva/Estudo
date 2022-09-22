
//condição de se e senão

/*
if (false){
    document.write('Entrou dentro do bloco if (Verdadeiro)')
} else{
    document.write('Entrou dentro do bloco else (Falso)')
}*/



//verificação com uma expressão de comparação

/*if (2 == 2){
    document.write('Entrou dentro do bloco if (Verdadeiro)')
} else{
    document.write('Entrou dentro do bloco else (Falso)')
}*/


//A utilização do comparativo === é identico é igual e do mesmo tipo

/*if (2 === '2'){
    document.write('Entrou dentro do bloco if (Verdadeiro)')
} else{
    document.write('Entrou dentro do bloco else (Falso)')
}*/

var num1 = prompt('Digite o 1º numero: ')
var num2 = prompt('Digite o 2º numero: ')

if (num1 > num2){
    document.write('<h2>O 1º numero: ' + num1 + ' é maior que o 2º numero: ' + num2 +'. </h2> <br>')
}else if (num1 < num2){
    document.write('<h2>O 2º numero: ' + num1 + ' é maior que o 1º numero: ' + num2 +'. </h2> <br>')
}else{
    document.write('<h2>O 1º numero: ' + num1 + ' é igual ao 2º numero: ' + num2 +'. </h2> <br>')
}

