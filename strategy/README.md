# O padrão Strategy

Este padrão pode ser utilizado quando se quer variar um comportamento de um objeto em tempo de execução, permitindo que diferentes **estratégias** sejam implementadas sem que para isso seja necessário alterar o código do objeto em questão. Enquanto algumas linguagens utilizam [*interfaces*](https://pt.wikipedia.org/wiki/Interface_(programa%C3%A7%C3%A3o_orientada_a_objetos)) para definir uma estrutura padrão a ser seguida por todas as estratégias, em python é possível usar classes [ABC](https://docs.python.org/3/library/abc.html), [duck typing](https://pt.wikipedia.org/wiki/Duck_typing) ou ainda sua "versão tipada", a classe [Protocol](https://www.python.org/dev/peps/pep-0544/).


No [Exemplo 1](./exemplo1.py) os comportamentos de *voar* e *grasnar* dos patos são modificados conforme a situação.

No [Exemplo 2](./exemplo2.py) a função *calculate* consegue realizar diferentes operações matemáticas apenas plugando as funções que respectivamente as implementam.