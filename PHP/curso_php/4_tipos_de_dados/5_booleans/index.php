<?php
    echo"<h1> Trabalhando com Valores Boleanos (Verdadeiro ou Falso)</h1>";
    echo "<hr>";

    echo "OS valores boleanos são falso (False) e verdadeiro (True).";

    // True retorna 1 pois na logica boelana 1 é igual a verdadeiro
    echo "<br>O valor true é igual a: ", true;

    // False não retorna nada pois false é igual a ZERO ou nada.
    echo "<br>O valor false é igual a: ", false;

    $condicao = True;

    // Usando a função is_bool() conseguimos identificar se é um boleano
    if (is_bool($condicao)) {
        echo "<br>A condição é Boleana";
    } else {
        echo "<br>A condição não é Boleana";
    }

    $numero = 2;

    // A estrutura de decisão IF trabalha com condições verdadeiras ou falsas
    // sendo assim ao validar que a condição é verdadeira ele entra e executa o 
    // bloco de código dentro das chaves. 
    if ($numero == 0) {
        echo "<br>Condição verdadeira ou True";
    } else {
        echo "<br>Condição falsa ou False";
    }

