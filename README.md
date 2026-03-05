# Проект на Python

Набор учебных функций для работы с выборкой и базовыми статистиками (mean, median, variance, std, trimmed mean и др.).

## Структура проекта

- `src/` — исходный код
  - `core/` — ядро приложения
  - `parsers/` — парсеры/обработчики
  - `storage/` — работа с хранением данных
  - `cli/` — CLI-интерфейс (`python -m src.cli.app demo`)
- `notebooks/` — ноутбуки (например, для Google Colab)
- `data/` — данные (сам каталог в Git, содержимое игнорируется)
- `tests/` — тесты (в т.ч. smoke-тест для CLI)
- `docs/` — документация
- `configs/` — конфигурационные файлы

## Быстрый старт

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows PowerShell
pip install -r requirements.txt
```

## Запуск CLI

```bash
python -m src.cli.app demo
```

## Запуск тестов

```bash
pytest
```

