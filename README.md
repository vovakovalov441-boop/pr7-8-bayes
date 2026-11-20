# ПР 7-8. Формула повної ймовірності та формула Байєса в ймовірнісній класифікації та діагностиці програмних систем

Ковальов Володимир, група ЗІПЗ-25-1. Варіант 13: Блок 2 — варіант 2 (точність аналізатора коду SAST), Блок 4 — варіант 2 (локалізація дефекту в розподіленій системі).

## Що робить програма
| Блок | Файл | Зміст |
|---|---|---|
| 1 | `PythonApplication1.py` | WAF/IDS: три гіпотези, частота ознаки A і апостеріорні частоти W(Hi\|A) для N = 100…10⁶, графік збіжності W(H3\|A) до 0,3830 |
| 2 | `block2_variants.py` | SAST: P(A) = 0,064, Precision P(H1\|A) ≈ 0,7031, помилки I і II роду, N = 100 000 |
| 3 | `PythonApplication1.py` | Naive Bayes Spam / Ham за словами «free», «click»: матриця помилок, Accuracy, Precision, Recall, F1 |
| 4 | `PythonApplication1.py` | Локалізація причини збою (баг / конфігурація / залізо) за формулою Байєса, 100 000 аварій |

## Запуск
```
pip install -r requirements.txt
cd PythonApplication1
python PythonApplication1.py
```
Результати виводяться в консоль, графік збіжності (Блок 1) зберігається в `PythonApplication1/graphics/simulation_results.png`.

## Структура
```
├── PythonApplication1.sln
├── PythonApplication1/
│   ├── PythonApplication1.py
│   ├── block2_variants.py
│   └── graphics/simulation_results.png
├── report/
│   └── PR7-8_Report_Kovalov_Volodymyr.pdf
├── README.md
├── requirements.txt
└── .gitignore
```
