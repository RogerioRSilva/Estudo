//nome

console.log(process.argv)

const args = process.argv.slice(2)

console.log(args)

const nome = args[0].split('=')[1]

console.log(nome)

//Usa-se o comando direto no terminal por exemplo
// node index.js nome=Rogério, idade=38

const idade = args[1].split('=')[1]

console.log(idade)