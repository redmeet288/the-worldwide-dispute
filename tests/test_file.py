import builtins
from typing import List

from src.file import main


def test_main_returns_message(capsys) -> None:
    """
    Базовый тест для функции main.
    Проверяем, что:
    - функция возвращает ожидаемую строку
    - строка выводится в stdout
    """
    result = main()

    captured = capsys.readouterr()

    assert result == "hello from file.py"
    assert "hello from file.py" in captured.out

