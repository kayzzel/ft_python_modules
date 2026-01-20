from typing import Generator


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int) -> Generator[int, None, None]:
    while (n > 0):
        nbr: int = 2
        divider: int = 2
        limit: int = nbr // 2
        is_prime: bool = True
        while (divider < limit):
            if nbr % divider == 0:
                is_prime = False
                break
            divider += 1
        if is_prime:
            yield nbr
            n -= 1
