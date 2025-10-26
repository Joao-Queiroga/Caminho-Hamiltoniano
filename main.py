import sys
from typing import List, Dict, Optional


def read_graph_from_lines(lines: List[str]):
    it = iter(
        [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]
    )
    try:
        header = next(it)
    except StopIteration:
        raise ValueError("Entrada vazia")
    parts = header.split()
    if len(parts) < 3:
        raise ValueError("Cabeçalho inválido. Esperado: n m d")
    n = int(parts[0])
    m = int(parts[1])
    directed = bool(int(parts[2]))
    adj: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        try:
            u, v = next(it).split()
            u = int(u)
            v = int(v)
        except StopIteration:
            break
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    for k in adj:
        adj[k].sort()
    return n, adj, directed


def find_hamiltonian_path(n: int, adj: Dict[int, List[int]]) -> Optional[List[int]]:
    visited = [False] * (n + 1)
    path: List[int] = []

    order = sorted(range(1, n + 1), key=lambda x: len(adj[x]))

    def backtrack(u: int) -> bool:
        visited[u] = True
        path.append(u)
        if len(path) == n:
            return True
        neighbors = sorted(adj[u], key=lambda x: len(adj[x]))
        for v in neighbors:
            if not visited[v]:
                if backtrack(v):
                    return True
        visited[u] = False
        path.pop()
        return False

    for start in order:
        path.clear()
        for i in range(len(visited)):
            visited[i] = False
        if backtrack(start):
            return path.copy()
    return None


if len(sys.argv) >= 2:
    fname = sys.argv[1]
    with open(fname, "r", encoding="utf-8") as f:
        lines = f.readlines()
else:
    print("Digite a entrada (Ctrl+D para terminar):")
    lines = sys.stdin.readlines()

try:
    n, adj, directed = read_graph_from_lines(lines)
except Exception as e:
    print("Erro ao ler grafo:", e)
    sys.exit(1)

path = find_hamiltonian_path(n, adj)
if path:
    print("Caminho Hamiltoniano encontrado:", " ".join(map(str, path)))
else:
    print("Caminho Hamiltoniano não existe.")
