//Condição de oepração E é usado o simbolo: &&

/*if (2 == 2 && 3 >= 1){
    document.write('<h3 class="bg-success text-white text-center">Verdadeiro</h3>')
}else{
    document.write('<h3 class="bg-danger text-dark text-center">Falso</h3>')
}*/



/*if (2 == 2 && 3 >= 1 && 'a' == 'b'){
    document.write('<h3 class="w-50 bg-success text-white text-center">Verdadeiro</h3>')
}else{
    document.write('<h3 class="w-50 bg-danger text-white text-center">Falso</h3>')
}*/


//Condição de oepração OU é usado o simbolo: ||
/*
if (2 == 2 || 3 >= 8 || 'a' == 'b'){
    document.write('<h3 class="w-50 bg-success text-white text-center">Verdadeiro</h3>')
}else{
    document.write('<h3 class="w-50 bg-danger text-white text-center">Falso</h3>')
}*/

// Condição de operação de negação é usado o simbolo: !
/*
if (!(2 == 2)){
    document.write('<h3 class="w-50 bg-success text-white text-center">Verdadeiro</h3>')
}else{
    document.write('<h3 class="w-50 bg-danger text-white text-center">Falso</h3>')
}*/

var nome = prompt('Digite o nome do aluno(a): ')
var nota = prompt('Digite a nota do aluno(a): ')
var faltas = prompt('Digite a qtdade de faltas do aluno(a): ')
var media = 7
var faltas_max = 15


if (nota >= media && faltas <= faltas_max){
    document.write('Nome do Aluno(a): ' + nome +'<br>')
    document.write('Nota Final: ' + nota +'<br>')
    document.write('Quantidade de Faltas: ' + faltas +'<br>')
    document.write('<h1 class="w-50 bg-success text-white text-center">APROVADO</h1>')
}else{
    document.write('Nome do Aluno(a): ' + nome +'<br>')
    document.write('Nota Final: ' + nota +'<br>')
    document.write('Quantidade de Faltas: ' + faltas +'<br>')
    document.write('<h1 class="w-50 bg-danger text-white text-center">REPROVADO</h1>')
}


//Operador ternário pode ser usado com a seguinte sintax

//variavale = (condição) ? <VERDADEIRO> : <FALSO>

var resultado = (nota >= media && falta <= faltas_max)? 'Aprovado' : 'Reprovado'