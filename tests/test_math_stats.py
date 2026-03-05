from src.math_stats import (
    approx,
    describe,
    mean,
    median,
    run_all_tests,
    std_sample,
    trimmed_mean,
    variance_sample,
    with_outlier,
)


def test_core_functions_basic() -> None:
    values = [10, 11, 9, 10, 12, 9, 10, 11, 10, 9]

    assert approx(mean(values), 10.1)
    assert median(values) == 10.0

    var = variance_sample(values)
    std = std_sample(values)
    assert var > 0
    assert std > 0

    values_out = with_outlier(values, 100)
    assert len(values_out) == len(values) + 1
    assert median(values_out) == 10.0

    d = describe(values)
    assert d["n"] == len(values)
    assert d["min"] == min(values)
    assert d["max"] == max(values)


def test_block04_lesson01_run_all_tests(capsys) -> None:
    run_all_tests()
    captured = capsys.readouterr()
    assert "BLOCK04 LESSON01: all tests passed" in captured.out

