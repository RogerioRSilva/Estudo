var idade = prompt('Qual a sua idade: ')

if (idade >= 0 && idade < 15){
    document.write('<h3 class="w-50 bg-info text-center"> Sua idade é: ' + idade + '</h3> <br>')
    document.write('<h3 class="bg-success text-white text-center text-uppercase">Você é criança!!!</h3>')
}else if(idade >= 15 && idade < 30){
    document.write('<h3 class="w-50 bg-info text-center"> Sua idade é: ' + idade + '</h3> <br>')
    document.write('<h3 class="bg-success text-white text-center text-uppercase">Você é jovem!!!</h3>')
}else if(idade >=30 && idade < 60){
    document.write('<h3 class="w-50 bg-info text-center"> Sua idade é: ' + idade + '</h3> <br>')
    document.write('<h3 class="bg-success text-white text-center text-uppercase">Você é adulto!!!</h3>')
}else{
    document.write('<h3 class="w-50 bg-info text-center"> Sua idade é: ' + idade + '</h3> <br>')
    document.write('<h3 class="bg-success text-white text-center text-uppercase">Você é idoso!!!</h3>')
}