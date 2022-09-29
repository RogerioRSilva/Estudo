// var nome = window.prompt('Qual é seu nome?')

// window.alert(`É um prazer te conhecer ${nome}`)

//parseInt - Converte o numero sempre em inteiro
//parseFloat - Converte o numero sempre em fluatuante
//Number - Generaliza todos os numeros e resultados
//String - Converte em string
//.toString - Converte em string
// String Formatada - (``) sempre usando crase e 
// as variáveis com ->Placeholder ${}

//length - é utlizado para contar os caracteres da string
//toUpperCase - Transforma todos os caracteres em maiusculos
// document.write(`Seu nome tem ${nome.length} letras. <br>`)
// document.write(`Seu nome em maiúsculo é ${nome.toUpperCase()}`)
// toFixed() - É utilizado para acrescentar 
// casas decimais no numero
//.replace - Substitui um caracter por outro
var nome = 'Rogério'

document.write(`Seu nome: ${nome.replace('Rogério', 'Heloisa')}`)

var valor = 1543.50

//Conversão do valor em moeda local BRL, USD, EUR , usando a localização pt_BR
document.write('<br>',valor.toLocaleString('pt-BR', {style:'currency', currency:'BRL'}))



