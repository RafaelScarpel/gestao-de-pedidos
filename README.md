# Visão Geral
Esse repositório contém o código desenvolvido para uma resolver uma prova da matéria de Programação Orientada a Objetos, feita em python.

# Objetivo
O exercício proposto era implementar um sistema de gestão de pedidos para uma loja fictícia de computadores, que vende desktops montados a partir de componentes individuais. O sistema verifica se os pedidos estão completos, e calcula os valores com impostos conforme as regras de negócio que foram especificadas.

## Funcionalidades:
### Verificação de pedidos
O sistema garante que cada pedido contenha todos os componentes necessários:
Gabinete (código 100-199); Placa-mãe (código 200-299); Processador (código 300-399);SSD (código 400-499); Memória RAM (código 500-599); Sistema Operacional (código 600-699);

### Cálculo de impostos
O sistema deve considerar os impostos de cada categoria de produtos para o cálculo do preço, com a seguinte regra:
Hardware: 6% para produtos até R$499,99 e 9% acima;  
Software: 5% para produtos até R$399,99 e 7% acima

### Relatório
O sistema gera uma impressão detalhada dos pedidos
