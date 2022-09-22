//abaixo está o modulo que foi importado do node.js


const fs = require('fs') //file system 

//chamando uma das funções do modulo que faz a leitura do arquivo.txt

fs.readFile('arquivo.txt', 'utf8', (err, data) => {
    if(err){
        console.log(err)
    }
    console.log()
    console.log(data)
    console.log()

})