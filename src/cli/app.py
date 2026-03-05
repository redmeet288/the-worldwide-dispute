import argparse
import sys
from typing import List, Optional


def main(argv: Optional[List[str]] = None) -> int:
    """
    Минимальный CLI, который можно запустить так:

        python -m src.cli.app demo

    Сейчас поддерживается одна команда: `demo`.
    """
    parser = argparse.ArgumentParser(prog="src-cli", description="Demo CLI for the project.")
    parser.add_argument(
        "command",
        help="Название команды. Сейчас поддерживается только 'demo'.",
    )

    args = parser.parse_args(argv)

    if args.command == "demo":
        print("Demo command executed")
        return 0

    print(f"Unknown command: {args.command}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

