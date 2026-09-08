from collections import deque
import time
import sys


def get_new_data():
    with open("/home/aluno/trabalho/lista.txt", "r") as file:
        data = file.readlines()

    data = [line.strip() for line in data]

    return data


positions = [0, 99, 999, 4999]


# =========================
# HASH TABLE
# =========================

hashtable = {}
hash_data = get_new_data()

# ADICAO
started_at = time.time()

for i, value in enumerate(hash_data):
    hashtable[i] = value

finished_at = time.time()

print("HASHTABLE")
print("Adicao")
print("Tempo de execucao:", finished_at - started_at, "segundos")
print("Memoria utilizada:", sys.getsizeof(hashtable), "bytes")
print()

# POSICOES
for pos in positions:
    print("Posicao", pos + 1, ":", hashtable[pos])

print("Ultima posicao:", list(hashtable.values())[-1])
print()

# REMOCAO
hash_remocao = hashtable.copy()

started_at = time.time()

for i in list(hash_remocao.keys()):
    del hash_remocao[i]

finished_at = time.time()

print("Remocao")
print("Tempo de execucao:", finished_at - started_at, "segundos")
print("Memoria utilizada:", sys.getsizeof(hash_remocao), "bytes")
print()


# =========================
# PILHA
# =========================

pilha = []
pilha_data = get_new_data()

# ADICAO
started_at = time.time()

for value in pilha_data:
    pilha.append(value)

finished_at = time.time()

print("PILHA")
print("Adicao")
print("Tempo de execucao:", finished_at - started_at, "segundos")
print("Memoria utilizada:", sys.getsizeof(pilha), "bytes")
print()

# POSICOES
print("Posicoes")

pilha_posicoes = pilha.copy()

started_at = time.time()

for pos in positions:
    temp = pilha_posicoes.copy()

    for i in range(len(pilha_posicoes) - 1 - pos):
        temp.pop()

    print("Posicao", pos + 1, ":", temp[-1])

finished_at = time.time()

print("Tempo de execucao:", finished_at - started_at, "segundos")
print()

# REMOCAO
pilha_remocao = pilha.copy()

started_at = time.time()

while pilha_remocao:
    pilha_remocao.pop()

finished_at = time.time()

print("Remocao")
print("Tempo de execucao:", finished_at - started_at, "segundos")
print("Memoria utilizada:", sys.getsizeof(pilha_remocao), "bytes")
print()

# =========================
# FILA
# =========================

fila = deque()
fila_data = get_new_data()

# ADICAO
started_at = time.time()

for value in fila_data:
    fila.append(value)

finished_at = time.time()

print("FILA")
print("Adicao")
print("Tempo de execucao:", finished_at - started_at, "segundos")
print("Memoria utilizada:", sys.getsizeof(fila), "bytes")
print()

# POSICOES
print("Posicoes")

fila_posicoes = fila.copy()

started_at = time.time()

for pos in positions:
    temp = fila_posicoes.copy()

    for i in range(pos):
        temp.popleft()

    print("Posicao", pos + 1, ":", temp[0])

finished_at = time.time()

print("Tempo de execucao:", finished_at - started_at, "segundos")
print()

# REMOCAO
fila_remocao = fila.copy()

started_at = time.time()

while fila_remocao:
    fila_remocao.popleft()

finished_at = time.time()

print("Remocao")
print("Tempo de execucao:", finished_at - started_at, "segundos")
print("Memoria utilizada:", sys.getsizeof(fila_remocao), "bytes")
print()
