from itertools import combinations

lista = [5, 3, 1, 7, 5, 9]


def diferenca_absoluta(lista: list,
                       allow_duplicates: bool = False,
                       sorted_pairs: bool = True,
                       unique_pairs: bool = True):
    # Ordena os valores da lista de forma crescente e faz os pares da mesma forma
    if sorted_pairs is True:
        lista = sorted(lista)

    # Cria as combinações possiveis dos valores da lista
    combinacoes = list(combinations(lista, 2))

    # Remove combinações de valores duplicados que geram valores de diferença absoluta igual a 0 ou pares que já existam
    if allow_duplicates is False:
        combinacoes_sem_duplicatas = []
        for comb in combinacoes:
            if comb[0] != comb[1]:
                combinacoes_sem_duplicatas.append(comb)
        combinacoes = combinacoes_sem_duplicatas

    # Cria uma lista com as diferenças absoluta de cada par
    diferencas = [
        abs(combinacao[0] - combinacao[1]) for combinacao in combinacoes
    ]
    # Gera a lista com o(s) par(es) com a menor diferença absoluta
    pares_menores = []
    for comb in combinacoes:
        if abs(comb[0] - comb[1]) == min(diferencas):
            pares_menores.append(comb)

    # Filtra o resultado para garantir somentes pares unicos como resultado final
    if unique_pairs is True:
        pares_unicos = []
        for pares in pares_menores:
            if pares not in pares_unicos and tuple(reversed(pares)) not in pares_unicos:
                pares_unicos.append(pares)
        pares_menores = pares_unicos
    return pares_menores


print(diferenca_absoluta(lista))
