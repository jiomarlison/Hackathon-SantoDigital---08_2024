from itertools import combinations

lista = [45, 6, 3, 2, 9]


def combinacoes(lista: list,
                max_size: int = 0,
                min_size: int = 0,
                distinct_only: bool = False,
                sort_subsets: bool = False):
    for valor in lista:
        print(valor)
    combinacoes = list(combinations(lista, 2))


combinacoes(lista)
