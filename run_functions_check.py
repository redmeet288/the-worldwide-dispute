from __future__ import annotations

import sys
from pathlib import Path

from src.analytics import build_binary_counts, laplace_smooth_prob, score_buy_probability
from src.math_stats import (
    approx,
    bayes_posterior,
    describe,
    mean,
    median,
    prob_from_counts,
    std_sample,
    trimmed_mean,
    variance_sample,
    with_outlier,
)


def main() -> int:
    # Гарантируем, что при запуске из корня репозитория импорт `src.*` будет работать.
    repo_root = Path(__file__).resolve().parent
    sys.path.insert(0, str(repo_root))

    # 1) Проверка статистических функций (аналог run_all_tests(), но без печати ✅).
    s = [10, 11, 9, 10, 12, 9, 10, 11, 10, 9]

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

    print("Stats checks: OK")

    # 2) Пример из ноутбука: события (clicked, bought).
    records = [
        {"clicked": 1, "bought": 1},
        {"clicked": 1, "bought": 0},
        {"clicked": 1, "bought": 1},
        {"clicked": 0, "bought": 0},
        {"clicked": 1, "bought": 0},
        {"clicked": 0, "bought": 0},
        {"clicked": 1, "bought": 1},
        {"clicked": 0, "bought": 0},
        {"clicked": 1, "bought": 0},
        {"clicked": 1, "bought": 1},
        {"clicked": 0, "bought": 0},
        {"clicked": 1, "bought": 0},
    ]

    print("\n=== Bayes/frequencies: clicked -> bought ===")

    counts = build_binary_counts(records, a_key="bought", b_key="clicked")
    print("counts =", counts)
    assert counts["n"] == 12
    assert counts["count_A"] == 4  # bought=1
    assert counts["count_B"] == 8  # clicked=1
    assert counts["count_A_and_B"] == 4

    # P(bought) и P(clicked) по частотам
    p_bought = prob_from_counts(counts["count_A"], counts["n"])
    p_clicked = prob_from_counts(counts["count_B"], counts["n"])

    # Likelihood: P(clicked|bought) = count(A∩B)/count(A)
    p_clicked_given_bought = counts["count_A_and_B"] / counts["count_A"]

    # Posterior: P(bought|clicked)
    posterior = bayes_posterior(
        prior=p_bought,
        likelihood=p_clicked_given_bought,
        evidence=p_clicked,
    )
    print("P(bought)               =", p_bought)
    print("P(clicked)              =", p_clicked)
    print("P(clicked|bought)      =", p_clicked_given_bought)
    print("P(bought|clicked)      =", posterior)

    # Проверка: прямой подсчёт P(bought|clicked) = count(A∩B)/count(B)
    direct = counts["count_A_and_B"] / counts["count_B"]
    assert approx(direct, posterior)
    print("direct P(bought|clicked) =", direct)
    print("approx(diff)              =", abs(direct - posterior))

    # 3) Наивный скоринг: P(buy | clicked=value)
    p_buy_click1 = score_buy_probability(records, clicked_value=1)
    p_buy_click0 = score_buy_probability(records, clicked_value=0)
    print("\n=== Naive scoring ===")
    print("P(buy | click=1) =", p_buy_click1)
    print("P(buy | click=0) =", p_buy_click0)
    assert approx(p_buy_click1, 0.5)
    assert approx(p_buy_click0, 0.0)

    # 4) Лапласовское сглаживание для click=0
    subset0 = [r for r in records if int(r["clicked"]) == 0]
    succ0 = sum(1 for r in subset0 if int(r["bought"]) == 1)
    trials0 = len(subset0)
    p_smooth0 = laplace_smooth_prob(successes=succ0, trials=trials0)
    print("\n=== Laplace smoothing (for click=0) ===")
    print("raw P(buy|click=0)    =", p_buy_click0)
    print("smooth P(buy|click=0) =", p_smooth0)
    assert p_smooth0 > p_buy_click0

    print("\nOK: Function check finished successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

