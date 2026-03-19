from __future__ import annotations


def build_binary_counts(recs: list[dict], a_key: str, b_key: str) -> dict:
    """Построить счётчики для бинарных признаков A и B."""
    n = len(recs)
    count_A = 0
    count_B = 0
    count_A_and_B = 0

    for r in recs:
        a = int(r[a_key])
        b = int(r[b_key])
        if a not in (0, 1) or b not in (0, 1):
            raise ValueError("build_binary_counts: values must be 0/1")
        if a == 1:
            count_A += 1
        if b == 1:
            count_B += 1
        if a == 1 and b == 1:
            count_A_and_B += 1

    return {
        "n": n,
        "count_A": count_A,
        "count_B": count_B,
        "count_A_and_B": count_A_and_B,
    }


def score_buy_probability(recs: list[dict], clicked_value: int) -> float:
    """Наивный скоринг P(buy | clicked=value)."""
    if clicked_value not in (0, 1):
        raise ValueError("clicked_value must be 0/1")
    subset = [r for r in recs if int(r["clicked"]) == clicked_value]
    if len(subset) == 0:
        raise ValueError("No records for clicked_value")
    bought_count = sum(1 for r in subset if int(r["bought"]) == 1)
    return bought_count / len(subset)


def laplace_smooth_prob(successes: int, trials: int) -> float:
    """
    Сглаживание Лапласа: P = (successes + 1) / (trials + 2).
    """
    if trials < 0 or successes < 0 or successes > trials:
        raise ValueError("laplace_smooth_prob: invalid counts")
    return (successes + 1) / (trials + 2)

