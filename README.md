# 🧭 Caminho Hamiltoniano em Python

## 📖 Descrição do projeto
Este projeto implementa um **algoritmo de busca por Caminho Hamiltoniano** em grafos **orientados ou não orientados**, utilizando a técnica de **backtracking**.

Um Caminho Hamiltoniano é uma sequência de vértices que visita **cada vértice exatamente uma vez**. O objetivo é determinar se tal caminho existe e, em caso afirmativo, exibir a sequência encontrada.

---

## 🔎 Lógica do algoritmo
1. **Leitura do grafo**: o programa lê o número de vértices, arestas e a informação se o grafo é dirigido ou não.
2. **Construção da lista de adjacência**: cria uma estrutura que representa as conexões entre os vértices.
3. **Busca com *backtracking***:
   - Começa a busca a partir de cada vértice do grafo.
   - Marca o vértice atual como visitado e adiciona-o ao caminho.
   - Tenta visitar recursivamente os vizinhos não visitados.
   - Se todos os vértices forem visitados, o caminho é Hamiltoniano.
   - Caso contrário, faz *backtrack* (desmarca o vértice e tenta outro caminho).
4. **Resultado**: exibe o caminho encontrado ou informa que não existe Caminho Hamiltoniano.

---

## 🧩 Implementação (linha a linha)
Arquivo: `main.py`

```python
def read_graph_from_lines(lines):
    it = iter([ln.strip() for ln in lines if ln.strip() and not ln.startswith('#')])
    header = next(it).split()
    n, m, directed = int(header[0]), int(header[1]), bool(int(header[2]))
    adj = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, next(it).split())
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return n, adj, directed
```

```python
def find_hamiltonian_path(n, adj):
    visited = [False] * (n + 1)
    path = []
    def backtrack(u):
        visited[u] = True
        path.append(u)
        if len(path) == n:
            return True
        for v in adj[u]:
            if not visited[v]:
                if backtrack(v):
                    return True
        visited[u] = False
        path.pop()
        return False
    for start in range(1, n+1):
        path.clear()
        visited = [False] * (n + 1)
        if backtrack(start):
            return path.copy()
    return None
```

```python
    lines = sys.stdin.readlines()
    n, adj, _ = read_graph_from_lines(lines)
    path = find_hamiltonian_path(n, adj)
    if path:
        print(":", " ".join(map(str, path)))
    else:
        print("No Hamiltonian path exists.")
```

---

## ▶️ Como executar o projeto

1. **Clone o repositório:**
```bash
git clone https://github.com/SEU_USUARIO/caminho-hamiltoniano.git
cd caminho-hamiltoniano
```

2. **Execute o programa:**
```bash
python3 main.py entrada.txt
```

Ou digite a entrada manualmente:
```bash
python3 main.py
```

3. **Formato de entrada:**
```
n m d
u v
...
```

- `n`: número de vértices
- `m`: número de arestas
- `d`: 0 = não orientado | 1 = orientado

**Exemplo:**
```
4 4 0
1 2
2 3
3 4
4 1
```

---

## 📊 Relatório Técnico

### 🔹 Classes de Complexidade
O **problema do Caminho Hamiltoniano** pertence à classe **NP-Completo**.

- Está em **NP**, pois, dado um caminho, é possível verificar em tempo polinomial se ele visita todos os vértices exatamente uma vez.
- É **NP-Completo**, pois o **Problema do Caixeiro Viajante (TSP)** pode ser reduzido a ele.
  O TSP adiciona pesos às arestas e busca o ciclo Hamiltoniano de custo mínimo — portanto, é uma generalização do Caminho Hamiltoniano.
- Assim, encontrar um Caminho Hamiltoniano é **tão difícil quanto qualquer problema em NP**.

---

### 🔹 Complexidade Assintótica de Tempo
O algoritmo de *backtracking* testa todas as permutações possíveis de vértices em casos extremos.

Cada vértice pode ser o início do caminho e o algoritmo tenta todas as ordens possíveis:
```
T(n) ≈ O(n!)
```

O método usado para determinar essa complexidade é **contagem combinatória** (n vértices → n! possíveis caminhos).

Portanto, a **complexidade de tempo** é **O(n!)**, e a de espaço é **O(n)** (para armazenar o caminho e os vértices visitados).

---

### 🔹 Aplicação do Teorema Mestre
O **Teorema Mestre** não se aplica aqui, pois:
- O algoritmo **não possui recorrência do tipo** `T(n) = aT(n/b) + f(n)`.
- A busca é **combinatória** e não se baseia em divisão e conquista.

---

### 🔹 Casos de Complexidade

| Caso | Descrição | Complexidade |
|------|------------|---------------|
| **Melhor caso** | Caminho encontrado logo na primeira tentativa | O(n) |
| **Médio caso** | Caminho encontrado após várias tentativas | O(k·n) |
| **Pior caso** | Nenhum caminho Hamiltoniano encontrado | O(n!) |
