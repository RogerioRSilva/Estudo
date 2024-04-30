<?php

    $numero = 20;

    echo "<h3>Valor Digitado: {$numero}</h3>";

    // A função is_int() faz a validação e o numero é inteiro. 
    if (is_int($numero)) {
        echo "Numero é inteiro";
    }
    else {
        echo "Numero não é inteiro";
    }
?>