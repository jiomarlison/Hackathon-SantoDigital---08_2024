from itertools import combinations

lista = [5, 1, 4, 3, 3, 4, 1, 5, 6, 7]


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
            if comb[0] != comb[1] and comb not in combinacoes_sem_duplicatas:
                combinacoes_sem_duplicatas.append(comb)
        combinacoes = combinacoes_sem_duplicatas
    #Cria uma lista com as diferenças absoluta de cada par
    diferencas = [
        abs(combinacao[0] - combinacao[1]) for combinacao in combinacoes
    ]
    #Gera a lista com o(s) par(es) com a menor diferença absoluta
    pares_menor_diferenca = []
    for comb in combinacoes:
        if abs(comb[0] - comb[1]) == min(diferencas):
            pares_menor_diferenca.append(comb)
    #Filtra o resultado para garantir somentes pares unicos como resultado final
    if unique_pairs is True:
        pares_unicos = []
        for pares in pares_menor_diferenca:
            pares_unicos.append(tuple(sorted(pares)))
        pares_unicos = list(set(pares_unicos))
        pares_menor_diferenca = pares_unicos
    return pares_menor_diferenca


print(diferenca_absoluta(lista))
