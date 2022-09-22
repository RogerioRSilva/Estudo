//Acionando o modulo diretamente sem insatalação usando o 
// createInterface

const readline = require('readline').createInterface({
    input: process.stdin,  //entrada de dados
    output: process.stdout, //saída de dados
})


//Faz a leitura da entrada de dados direto sem argumento. 
//Metodo question funciona como pergunta a ser respondida.
//Language é uma váriavel para atribuição de dados e será lida por uma interpolção de dados. 
readline.question('Qual a sual linguagem preferida? ', (language) => {
    if(language === "Python"){
        console.log('Isso nem é linguagem!')
    }else{
        console.log(`A minha linguagem preferida é: ${language}`)
    }
    
    readline.close()
})