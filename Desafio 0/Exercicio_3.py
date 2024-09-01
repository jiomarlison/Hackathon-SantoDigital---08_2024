from itertools import combinations

lista = [6, 2, 3, 1]


def lista_combinacoes(lista: list[int],
                      max_size: int = len(lista),
                      min_size: int = 0,
                      distinct_only: bool = True,
                      sort_subsets: bool = True,
                      ):
    # Bloco de verificação para parametros invalidos
    for n in lista:
        if type(n) is not int:
            print("A lista só pode conter numeros!")
            return ""
    if len(lista) == 0:
        print("A lista deve conter ao menos 1 número!")
        return ""
    if min_size > max_size:
        print("Erro, tamanho minimo(min_size) não pode ser maior que maior tamanho(max_size)!")
        return ""
    if min_size < 0:
        print("Erro, tamanho minimo(min_size) não pode ser menor que 0!")
        return ""
    if max_size > len(lista):
        print("max_size não pode ser maior que a quantia de elementos da lista!")
        return ""

    # Remove números duplicados da lista, evitando a criação de dois conjuntos iguais
    # e/ou com dois ou mais números iguais em um unico conjunto.
    if distinct_only is True:
        nova_lista = []
        for numero in lista:
            if numero not in nova_lista:
                nova_lista.append(numero)
        lista = nova_lista

    # Ordena os números da lista de forma que os conjuntos gerados estarão em ordem
    # crescente tanto internamente em cada conjunto e externamente entre eles.
    if sort_subsets is True:
        lista = sorted(lista)

    # Realiza as combinações dos numeros da lista depois de passar por quais
    # parametro foram ativados
    combinacoes = []
    for tam in range(0, len(lista) + 1):
        if max_size >= tam >= min_size:
            for comb in combinations(lista, tam):
                combinacoes.append(comb)

    return combinacoes


print(lista_combinacoes(lista))
