from itertools import combinations
lista = [3, 5, 1, 4, 3, 5]
def diferenca_absoluta(lista: list, allow_duplicates=False, sorted_pairs=False, unique_pairs: bool = False):
    combinacoes = list(combinations(lista, 2))
    for combinacao in combinacoes:
        print(combinacao[0], combinacao[1])
        if not allow_duplicates:
            if combinacao[0] == combinacao[1]:
                print(f"{combinacao[0]} e {combinacao[1]} são iguais")
        if unique_pairs:
            if combinacao[0] == combinacao[1]:
                print(f"{combinacao[0]} e {combinacao[1]} são iguais")

        # print(
        #     combinacao[0] - combinacao[1] if combinacao[0] - combinacao[1] >= 0 else (combinacao[0] - combinacao[1]) * -1
        # )

diferenca_absoluta(lista)
