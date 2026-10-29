import inspect
import random
from typing import Any, Callable, Generator, Sequence


def curry(func: Callable[..., Any]) -> Callable[..., Any]:
    """Создает каррированную функцию произвольной арности (овышенная  3)."""
    if not callable(func):
        raise TypeError("ргумент func должен быть вызываемым объектом.")

    sig = inspect.signature(func)
    required_count = len([
        p for p in sig.parameters.values()
        if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
        and p.default is inspect.Parameter.empty
    ])

    def curried(*args: Any, **kwargs: Any) -> Any:
        if len(args) + len(kwargs) >= required_count:
            return func(*args, **kwargs)

        def inner(*more_args: Any, **more_kwargs: Any) -> Any:
            return curried(*(args + more_args), **{**kwargs, **more_kwargs})

        return inner

    return curried


def infinite_random_data_stream(
    categories: Sequence[str] = ("sensor_temp", "sensor_pressure", "sensor_humidity"),
    seed: int | None = 100,
) -> Generator[dict[str, Any], None, None]:
    """есконечный генератор случайных телеметрических пакетов (овышенная  7)."""
    if not isinstance(categories, (list, tuple)):
        raise TypeError("араметр categories должен быть списком или кортежем.")
    if not categories:
        raise ValueError("араметр categories не может быть пустым.")
    for cat in categories:
        if not isinstance(cat, str) or not cat.strip():
            raise ValueError("атегория должна быть непустой строкой.")

    rng = random.Random(seed)
    packet_id = 1
    while True:
        cat = rng.choice(categories)
        val = round(rng.uniform(15.0, 95.0), 2)
        yield {
            "packet_id": packet_id,
            "metric": cat,
            "value": val,
            "status": "OK" if val < 80.0 else "WARNING",
        }
        packet_id += 1
