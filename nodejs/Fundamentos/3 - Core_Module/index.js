//Costuma-se chamar sempre a constante "metodo" com 
//o mesmo nome no require
// const variavel = require('variavel')

const path = require('path')

//Verificar a extensão do arquivo
const extension = path.extname('arquivo.php')

console.log(extension)