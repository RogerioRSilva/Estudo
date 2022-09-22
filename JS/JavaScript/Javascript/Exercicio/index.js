var nome = prompt('Digite seu nome:')
var altura = prompt('Digite sua altura:')
var peso = prompt('Digite seu peso:')

altura /= 100

calculo = peso / (Math.pow(altura, 2))

if (calculo < 16) {
    document.write(nome, ' você possui indice de massa corporal igua a ', calculo, ', sendo classificado como ' + 'Baixo peso MUITO GRAVE.')
}
else if (calculo > 16 && calculo < 17) {

    document.write(nome, ' você possui indice de massa corporal igua a ', calculo, ', sendo classificado como ' + 'Baixo peso GRAVE.')
}
else if (calculo > 17 && calculo < 18.50) {
    document.write(nome, ' você possui indice de massa corporal igua a ', calculo, ', sendo classificado como ' + 'Baixo Peso')
}
else if (calculo >= 18.50 && calculo < 25) {
    document.write(nome, ' você possui indice de massa corporal igua a ', calculo, ', sendo classificado como ' + 'Peso Normal')
}
else if (calculo >= 25 && calculo < 30) {
    document.write(nome, ' você possui indice de massa corporal igua a ', calculo, ', sendo classificado como ' + 'Sobre Peso')
}
else if (calculo >= 30 && calculo < 35) {
    document.write(nome, ' você possui indice de massa corporal igua a ', calculo, ', sendo classificado como ' + 'Obesidade Grau I')
}
else if (calculo >= 35 && calculo < 40) {
    document.write(nome, ' você possui indice de massa corporal igua a ', calculo, ', sendo classificado como ' + 'Obesidade Grau II')
}
else if (calculo >= 40) {
    document.write(nome, ' você possui indice de massa corporal igua a ', calculo, ', sendo classificado como ' + 'Obesidade Grau III')
}

