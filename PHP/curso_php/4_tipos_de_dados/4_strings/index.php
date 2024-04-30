<?php
    // As strings tem como padrão utilizar aspas simples ou duplas
    echo "Aqui contem um texto que equivale a uma String.";

    $idade = 20;

    // Inserindo uma variavel dentro do texto. 
    echo "<br>A pessoa tem $idade anos";

    echo "<hr>";
    echo "<h2>Validando se é uma string</h2>";

    $texto = "Notebook";

    echo "O texto escrito é: $texto<br>";

    // Usando a função is_string() valida se o a variável é uma string.
    if (is_string($texto)){
        echo "O texto é uma string";
    }
    else{
        echo "O texto não é uma string";
    }