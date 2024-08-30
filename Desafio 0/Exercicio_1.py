def asterisco(n: int):
    return ['*' * i for i in range(1, n + 1)]


print(
    asterisco(
        int(
            input("Digite um número: ")
        )
    )
)
