# Simulação de Bebidas Quentes - Padrão Template Method

Projeto simples em Python que demonstra o padrão de projeto **Template Method**, aplicado a uma simulação de preparo de bebidas quentes (café e chá).

## O que é o Template Method?

É um padrão de projeto comportamental que define o **esqueleto de um algoritmo** em uma classe base, deixando que as subclasses implementem apenas os passos que variam entre elas, sem alterar a estrutura geral do algoritmo.

Nesse projeto:

- A classe abstrata `BebidaQuente` define o algoritmo geral de preparo (`preparar_bebida`), na ordem: **ferver água → misturar → servir**.
- O passo `ferver_agua` é igual para qualquer bebida quente, então já vem pronto na classe mãe.
- Os passos `misturar` e `servir` são marcados como `@abstractmethod`, ou seja, são obrigatórios, mas cada subclasse decide como implementá-los.
- As classes `Cafe` e `Cha` herdam de `BebidaQuente` e implementam `misturar` e `servir` do seu próprio jeito.

## Conceitos de POO aplicados

- **Classes abstratas** (`ABC`, `abstractmethod`)
- **Herança**
- **Polimorfismo** — o mesmo método `preparar_bebida()` produz resultados diferentes dependendo de qual objeto (café ou chá) o chama
- **Template Method** (padrão de projeto comportamental)

## Como executar

```bash
python template_method_bebidas.py
```

### Saída esperada

```
== Preparando café ==
1. Fervendo água a 100 graus celsius...
2. Misturando o pó de café com água quente...
3. Servindo na caneca grande com café.
--- Bebida pronta ---

== Preparando chá ==
1. Fervendo água a 100 graus celsius...
2. Misturando o chá na água quente...
3. Servindo o chá em uma caneca grande.
--- Bebida pronta ---
```

## Por que a classe base não pode ser instanciada?

`BebidaQuente` possui métodos abstratos (`misturar` e `servir`) sem implementação. Isso impede que ela seja instanciada diretamente — só é possível criar objetos de subclasses que implementem todos os métodos abstratos (como `Cafe` e `Cha`).

## Possíveis extensões

- Adicionar uma nova bebida (ex: `Chocolate`) implementando apenas `misturar` e `servir`
- Adicionar um passo opcional (hook), como `adicionar_extras`, que as subclasses podem sobrescrever se quiserem
