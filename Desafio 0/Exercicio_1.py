# Recebe um número e multiplica ele pela string "*"
def asterisco(n: int):
    # Faz um List Comprehension multiplicando n por "*" partindo de 1 ate n+1, já que python começa a contagem em 0
    # tivemos que forçar a comecar do 1 e incrementamos +1 ao valor de n para atingir o valor certo.
    return ['*' * i for i in range(1, n + 1)]


print(
    asterisco(
        int(
            input("Digite um número: ")
        )
    )
)
