<?php

    // Crie um array associativo com caracteristicas de uma pessoa;
    // Desafio: faça um if checando se ela é maior de idade e imprima uma
    // mensagem, caso seja

$pessoa = [
    "nome"=> "Juliana",
    "idade"=> 15,
    "sexo"=> "Feminino",
    "altura"=> 1.75,
    "nacionalidade"=> "Brasileira",
];

echo "<h2>Caracteristicas de uma pessoa</h2>";
echo "<hr>";
echo "<br>";

echo '<strong>Nome: </strong>', $pessoa['nome'];
echo '<br><strong>Idade: </strong>', $pessoa['idade'];
echo '<br><strong>Sexo: </strong>', $pessoa['sexo'];
echo '<br><strong>Altura: </strong>', $pessoa['altura'];
echo '<br><strong>Nacionalidade: </strong>', $pessoa['nacionalidade'];

echo '<hr>';
echo '<h3>A pessoa é maior de idade? </h3>';

if ($pessoa['idade'] > 18) {
    echo '<br>A pessoa é maior de idade pois tem ', $pessoa['idade'],' anos';
}else{
    echo '<br>A pessoa é menor de idade pois tem ', $pessoa['idade'],' anos';
}
