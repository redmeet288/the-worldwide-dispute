from src.cli.app import main


def test_cli_demo_command(capsys) -> None:
    """
    Smoke-тест для CLI: проверяем, что команда `demo` отрабатывает без ошибок.
    """
    exit_code = main(["demo"])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Demo command executed" in captured.out

