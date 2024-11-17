# **Otimização de Rotas de Entrega com IA**

## **Descrição**

Este projeto aborda o problema de **otimização de rotas de entrega** para múltiplos veículos, com o objetivo de minimizar a distância total percorrida e garantir que as entregas sejam realizadas de acordo com **restrições de capacidade** dos veículos e **horários de entrega** específicos de cada cliente. A solução implementa algoritmos de otimização e técnicas de IA para encontrar rotas eficientes e distribuí-las entre os veículos de forma a respeitar as capacidades e as janelas de entrega.

## **Funcionalidades**

- **Otimização de Rota**: Calcula as rotas mais curtas para múltiplos veículos, respeitando as distâncias entre os locais de entrega.
- **Capacidade dos Veículos**: Garante que as entregas atribuídas a cada veículo não excedam sua capacidade de carga.
- **Horários de Entrega**: Considera as janelas de horários de entrega para cada cliente, ajustando as rotas conforme as restrições de tempo.
- **Busca Local**: Aplica um algoritmo de busca local para otimizar as rotas e minimizar a distância percorrida.
- **Visualização**: Gera gráficos para visualização das rotas de entrega otimizadas.
- **Escalabilidade**: Fácil de adaptar para diferentes números de veículos, clientes e restrições.

## **Tecnologias Utilizadas**

- **Python**: Linguagem de programação principal.
- **NetworkX**: Para construção e manipulação do grafo de rotas.
- **Matplotlib**: Para visualização das rotas otimizadas.
- **Algoritmos de Otimização**: Dijkstra, Busca Local e técnicas de otimização de rotas.
- **Pandas**: Para manipulação de dados, se necessário.

## **Como Rodar**

### Pré-requisitos

1. Certifique-se de ter o Python 3.x instalado.
2. Instale as bibliotecas necessárias usando `pip`:

```bash
pip install networkx matplotlib pandas
```

### Execução

Para executar o projeto, basta rodar o script principal:

```bash
python otimizacao_rotas.py
```

Isso irá gerar a visualização das rotas otimizadas, levando em consideração as **restrições de capacidade** e **horários de entrega**.

### Personalização

Você pode personalizar os seguintes parâmetros no código:

- **Número de veículos** e suas capacidades.
- **Locais de entrega** e suas respectivas janelas de horário.
- **Distâncias entre os locais de entrega**.

Os dados de entrada são definidos no início do código, e você pode ajustar conforme suas necessidades.

## **Exemplo de Saída**

Após rodar o script, você verá:

1. A **atribuição inicial de entregas** para cada veículo.
2. A **atribuição otimizada de entregas** para cada veículo após a busca local.
3. A **distância total percorrida** antes e depois da otimização.
4. Um gráfico gerado pelo `matplotlib`, mostrando as **rotas otimizadas** no mapa.

## **Estrutura do Projeto**

```
/otimizacao_rotas
    |-- otimização_rotas.py       # Código principal do projeto
    |-- README.md                 # Este arquivo
    |-- data/
        |-- locais.csv            # Dados de locais e horários (opcional)
```
