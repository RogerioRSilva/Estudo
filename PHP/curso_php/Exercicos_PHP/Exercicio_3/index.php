<?php 
    // Crie um array associativo com as caracteristicas de um carro e as
    // exiba na pagina web.

$carro = [
    'marca' => 'Chevrolet', 
    'modelo' => 'Classic', 
    'ano' => 2011, 
    'cor' => 'Cinza', 
    'portas' => 4, 
    'combustivel' => 'Flex'
];

echo "<h1>Caracteristicas de um Carro</h1>";
echo "<hr>";
echo "<strong>Marca: </strong>", $carro['marca'];
echo "<br><strong>Modelo: </strong>", $carro['modelo'];
echo "<br><strong>Ano: </strong>", $carro['ano'];
echo "<br><strong>Cor: </strong>", $carro['cor'];
echo "<br><strong>Tipo Combustível: </strong>", $carro['combustivel'];
echo "<br><strong>Quantidade de Portas: </strong>", $carro['portas'];