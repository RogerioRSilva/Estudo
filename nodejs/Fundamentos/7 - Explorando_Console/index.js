const x = 10
const y = 'Algum texto'
const z = [1, 4]

console.log(x, y, z)

//Contagem de Impressão - Com o count ele retorna a contagem das saidas
console.count(`O valor de X é: ${x}`)
console.count(`O valor de X é: ${x}`)
console.count(`O valor de X é: ${x}`)
console.count(`O valor de X é: ${x}`)
console.count(`O valor de X é: ${x}`)

//Usando o código %s com poderá inserir uma váriável no final.
//Onde o sinal %s se torno o local onde a variável será inserida.
console.log('O nome é %s, e ele é um programador', y)

//Limpeza do console - setTimeout executa uma função após um certo tempo. 
setTimeout(() => {
    console.clear()
}, 5000)
