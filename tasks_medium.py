import random
from functools import reduce
from typing import Generator, Sequence


def sum_numbers_reduce(numbers: Sequence[int | float]) -> int | float:
    """ычисление суммы элементов последовательности через reduce (Средняя  3)."""
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("араметр numbers должен быть списком или кортежем.")
    if len(numbers) == 0:
        return 0
    for item in numbers:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(f"лемент {item} не является числом.")
    return reduce(lambda acc, x: acc + x, numbers, 0)


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """енератор n первых чисел ряда ибоначчи (Средняя  5)."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("оличество чисел n должно быть целым числом.")
    if n < 0:
        raise ValueError("оличество чисел n не может быть отрицательным.")

    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def random_range_generator(
    count: int,
    start: int = 1,
    end: int = 100,
    seed: int | None = 42,
) -> Generator[int, None, None]:
    """енератор случайных целых чисел в диапазоне [start, end] (Средняя  9)."""
    if not isinstance(count, int) or isinstance(count, bool):
        raise TypeError("араметр count должен быть целым числом.")
    if not isinstance(start, int) or isinstance(start, bool):
        raise TypeError("араметр start должен быть целым числом.")
    if not isinstance(end, int) or isinstance(end, bool):
        raise TypeError("араметр end должен быть целым числом.")
    if count < 0:
        raise ValueError("оличество чисел count не может быть отрицательным.")
    if start > end:
        raise ValueError("начение start не может быть больше end.")

    rng = random.Random(seed)
    for _ in range(count):
        yield rng.randint(start, end)
