from __future__ import annotations


def mean(values: list[float]) -> float:
    """Среднее арифметическое. Требует непустой список."""
    if len(values) == 0:
        raise ValueError("mean: empty list")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Медиана. Требует непустой список."""
    if len(values) == 0:
        raise ValueError("median: empty list")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return float(s[mid])
    else:
        return (s[mid - 1] + s[mid]) / 2


def variance_sample(values: list[float]) -> float:
    """Выборочная дисперсия (деление на n-1)."""
    n = len(values)
    if n < 2:
        raise ValueError("variance_sample: need at least 2 values")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / (n - 1)


def std_sample(values: list[float]) -> float:
    """Выборочное стандартное отклонение."""
    return variance_sample(values) ** 0.5


def with_outlier(values: list[float], outlier: float) -> list[float]:
    """Вернуть новую выборку, добавив выброс (не меняем исходный список)."""
    return list(values) + [outlier]


def trimmed_mean(values: list[float], k: int = 1) -> float:
    """Усечённое среднее: убрать k минимальных и k максимальных."""
    n = len(values)
    if n == 0:
        raise ValueError("trimmed_mean: empty list")
    if 2 * k >= n:
        raise ValueError("trimmed_mean: k too large")
    s = sorted(values)
    core = s[k : n - k]
    return mean(core)


def describe(values: list[float]) -> dict:
    """Короткое описание выборки (как мини-отчёт)."""
    return {
        "n": len(values),
        "min": min(values) if values else None,
        "max": max(values) if values else None,
        "mean": mean(values) if values else None,
        "median": median(values) if values else None,
        "std": std_sample(values) if len(values) >= 2 else None,
    }


def approx(a: float, b: float, eps: float = 1e-9) -> bool:
    """Проверка приблизительного равенства для тестов."""
    return abs(a - b) <= eps


def run_all_tests() -> None:
    """Воспроизведение блока автотестов из ноутбука."""
    s = [10, 11, 9, 10, 12, 9, 10, 11, 10, 9]

    assert len(s) == 10
    assert min(s) == 9
    assert max(s) == 12

    assert approx(mean(s), 10.1)
    assert median(s) == 10.0

    # mean=10.1, sum((x-m)^2)=8.9 => /9
    assert approx(round(variance_sample(s), 6), round(8.9 / 9, 6))
    assert approx(round(std_sample(s), 6), round((8.9 / 9) ** 0.5, 6))

    s2 = with_outlier(s, 100)
    assert len(s2) == 11
    assert approx(round(mean(s2), 6), round((sum(s) + 100) / 11, 6))
    assert median(s2) == 10.0  # медиана устойчива

    assert approx(trimmed_mean([1, 2, 3, 100], k=1), 2.5)
    assert trimmed_mean([1, 2, 3, 4, 100, 101], k=1) == mean([2, 3, 4, 100])

    d = describe(s)
    assert d["n"] == 10
    assert d["min"] == 9 and d["max"] == 12
    assert approx(d["mean"], 10.1)
    assert d["median"] == 10.0
    assert d["std"] is not None

    print("✅ BLOCK04 LESSON01: all tests passed")


if __name__ == "__main__":
    run_all_tests()

