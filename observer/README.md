# O padrão Observer

Este padrão pode ser utilizado quando existe um objeto que precisa notificar e atualizar outros objetos sempre que seu estado muda. Nesse contexto temos o subject (ou observable), responsável por notificar outros objetos interessados em suas atualizações, e os observers, objetos que receberão as notificações do subject.

No [exemplo 1](./exemplo1.py) vemos a definição formal do pattern conforme a [GoF](http://wiki.c2.com/?GangOfFour), com as interfaces Subject e Observer definindo os métodos necessários para manipular e notificar os observadores.

O [exemplo 2](./exemplo2.py) foi extraído do livro [Use a Cabeça - Padrões de Projetos](https://altabooks.com.br/produto/use-a-cabeca-padroes-de-projetos/) e simula diferentes formas de exibir em tempo real informações extraídas de uma estação meteorológica.

Já o [exemplo 3](./exemplo3.py) implementa um sistema de email marketing de uma loja, permitindo que clientes se cadastrem e recebam as ofertas das campanhas promocionais em seus emaiis.