from itertools import combinations

lista = [45, 6, 3, 6]


def lista_combinacoes(lista: list,
                      max_size: int = 1,
                      min_size: int = -1,
                      distinct_only: bool = True,
                      sort_subsets: bool = True,
                      ):

    print("Erro, min_size não pode ser maior que max_size") if min_size > max_size else ...
    print("max_size não pode ser maior que a quantia de elementos da lista") if max_size > len(lista) else ...

    if distinct_only is True:
        nova_lista = []
        for numero in lista:
            if numero not in nova_lista:
                nova_lista.append(numero)
        lista = nova_lista
    if sort_subsets is True:
        lista = sorted(lista)

    combinacoes = []
    for tam in range(0, len(lista) + 1):
        if max_size >= tam >= min_size:
            for comb in combinations(lista, tam):
                combinacoes.append(comb)

    return combinacoes


print(lista_combinacoes(lista, 3, 1, True, True))
