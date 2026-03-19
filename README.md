# Проект на Python

Учебный проект на Python: базовые статистики и примеры вероятностного/байесовского скоринга.

## Структура проекта

- `src/` — исходный код (Python-пакет)
  - `core/` — ядро приложения
  - `parsers/` — парсеры/обработчики
  - `storage/` — работа с хранением данных
  - `cli/` — CLI-интерфейс (`python -m src.cli.app demo`)
  - `file.py` — простая функция/точка входа (используется тестами)
  - `math_stats.py` — статистические функции и Байес (`mean`, `median`, `prob_from_counts`, `bayes_posterior`, и т.д.)
  - `analytics.py` — функции для байесовского/частотного скоринга по бинарным событиям (`build_binary_counts`, `score_buy_probability`, `laplace_smooth_prob`)
- `notebooks/` — ноутбуки (например, для Google Colab)
- `data/` — данные (сам каталог в Git, содержимое игнорируется)
- `tests/` — тесты `pytest` и локальные учебные модули
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
