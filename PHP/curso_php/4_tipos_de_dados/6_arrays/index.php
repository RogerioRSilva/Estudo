<?php
    // Como boa pratica um Array deve manter sempre o mesmo tipo de dado.
    $lista = [10, 20, 30];

    // O Array não pode ser impresso pela função ECHO. 
    // Deve-se usar a função print_r =  Array ( [0] => 10 [1] => 20 [2] => 30 )
    print_r($lista);

    // Quando vamos exibir o item de dentro da lista podemos utilizar o ECHO
    // Exibindo o primeiro elemento da lista
    echo"<br> Primeiro Item da lista: ";
    echo $lista[0];


