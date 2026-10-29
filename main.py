from itertools import islice
from tasks_advanced import curry, infinite_random_data_stream
from tasks_medium import (
    fibonacci_generator,
    random_range_generator,
    sum_numbers_reduce,
)


def main() -> None:
    print("=== абораторная работа  4 (ариант 3) ===")

    # 1. Сумма через reduce (Средняя  3)
    data_list = [10, 20, 35, 45, -10]
    total = sum_numbers_reduce(data_list)
    print(f"[Средняя 3] Сумма элементов {data_list} через reduce = {total}")

    # 2. енератор ибоначчи (Средняя  5)
    fib_n = 8
    fib_res = list(fibonacci_generator(fib_n))
    print(f"[Средняя 5] енератор первых {fib_n} чисел ибоначчи: {fib_res}")

    # 3. енератор случайных чисел в диапазоне (Средняя  9)
    rnd_res = list(random_range_generator(count=6, start=10, end=50, seed=123))
    print(f"[Средняя 9] енератор псевдослучайных чисел [10, 50]: {rnd_res}")

    # 4. аррирование (овышенная  3)
    def calculate_volume(length: float, width: float, height: float) -> float:
        return length * width * height

    curried_volume = curry(calculate_volume)
    vol_step = curried_volume(2.5)(4.0)
    final_vol = vol_step(3.0)
    print(f"[овышенная 3] аррирование volume(2.5)(4.0)(3.0) = {final_vol}")

    # 5. есконечный генератор случайных данных (овышенная  7)
    stream = infinite_random_data_stream(seed=777)
    sample_packets = list(islice(stream, 4))
    print("[овышенная 7] акеты из бесконечного генератора данных:")
    for packet in sample_packets:
        print(f"  {packet}")


if __name__ == '__main__':
    main()
