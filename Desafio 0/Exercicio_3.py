from itertools import combinations

lista = [45, 6, 3, 4, 5, 3]


def lista_combinacoes(lista: list,
                      max_size: int = 1,
                      min_size: int = -1,
                      distinct_only: bool = False,
                      sort_subsets: bool = False
                      ):

    print("Erro, min_size não pode ser maior que max_size") if min_size > max_size else ...
    combinacoes = []
    for tam in range(0, len(lista) + 1):
        if max_size >= tam >= min_size:
            for comb in combinations(lista, tam):
                combinacoes.append(comb)

    if distinct_only is True:
        combinacoes_sem_duplicatas = []
        for comb in combinacoes:
            print(comb)

        combinacoes = combinacoes_sem_duplicatas
    return combinacoes


print(lista_combinacoes(lista, 3, 1, True))
