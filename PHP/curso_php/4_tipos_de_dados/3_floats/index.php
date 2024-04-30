<?php
    echo"<h1>Exibindo numeros flutuantes</h1>";
    echo "<hr>";

    echo "<strong>Numero flutuante (float): </strong>";
    echo 4.6;

    // Usamos a função is_float() para validar se é um float
    echo "<hr>";
    $numero = 5.9;
    echo "<h2>Valor inserido: {$numero}</h2>";

    if (is_float($numero)){
        echo "É um numero float";
    } else {
    echo "Não é um float";
    }
