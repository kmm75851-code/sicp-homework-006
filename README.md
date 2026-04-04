# Домашка 006 — Lists, Comprehension & Tuples

## Важно

Все функции **не изменяют** исходный список — они создают и возвращают **новый**.

❌ Нельзя использовать: `reversed()`, `.reverse()`, `zip()` — проверяется автоматически.

---

## Часть 1: `list_ops.py`

### `count_item(items, value)`

Считает, сколько раз `value` встречается в списке. Возвращает `int`.

```python
count_item([1, 2, 1, 3, 1], 1)   # → 3
count_item([1, 2, 1, 3, 1], 5)   # → 0
count_item([], 1)                 # → 0
```

💡 Заведи счётчик и пройди по списку циклом.

---

### `reverse_list(items)`

Возвращает **новый** список с элементами в обратном порядке.

```python
reverse_list([1, 2, 3])    # → [3, 2, 1]
reverse_list([])           # → []
```

💡 Можно идти с конца через `range(len(items)-1, -1, -1)`, или использовать срезы.

---

### `flatten_once(nested)`

Превращает список списков в плоский список — только один уровень.

```python
flatten_once([[1, 2], [3, 4], [5]])    # → [1, 2, 3, 4, 5]
flatten_once([[1, [2]], [3]])          # → [1, [2], 3]
flatten_once([])                       # → []
```

💡 Для каждого подсписка добавь его элементы через `result += sublist`.

---

### `chunk(items, n)`

Разбивает список на куски по `n` элементов. Последний кусок может быть короче.

```python
chunk([1, 2, 3, 4, 5], 2)    # → [[1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4], 2)       # → [[1, 2], [3, 4]]
chunk([1, 2, 3], 5)          # → [[1, 2, 3]]
chunk([], 3)                  # → []
```

💡 `range(0, len(items), n)` — шаг `n`. Добавляй срез `items[i:i+n]`.

---

### `interleave(a, b)`

Чередует элементы: `a[0], b[0], a[1], b[1], ...` Остаток длинного добавляется в конец.

```python
interleave([1, 2, 3], ['a', 'b', 'c'])      # → [1, 'a', 2, 'b', 3, 'c']
interleave([1, 2], ['a', 'b', 'c', 'd'])    # → [1, 'a', 2, 'b', 'c', 'd']
interleave([], [1, 2])                       # → [1, 2]
```

💡 Сначала `range(min(len(a), len(b)))` для пар, потом добавь хвост длинного.

---

### `run_length_encode(items)`

Подряд идущие одинаковые элементы схлопываются в пару `(количество, элемент)`.

```python
run_length_encode(['a', 'a', 'a', 'b', 'b', 'c'])    # → [(3, 'a'), (2, 'b'), (1, 'c')]
run_length_encode([1, 1, 2, 3, 3, 3])                 # → [(2, 1), (1, 2), (3, 3)]
run_length_encode([])                                  # → []
```

💡 Храни текущий элемент и счётчик. При смене — добавляй пару и сбрасывай счётчик.

---

### `rotate(items, k)`

Сдвигает список **вправо** на `k` позиций. Отрицательный `k` — влево.

```python
rotate([1, 2, 3, 4, 5], 2)     # → [4, 5, 1, 2, 3]
rotate([1, 2, 3, 4, 5], -1)    # → [2, 3, 4, 5, 1]
rotate([1, 2, 3], 0)           # → [1, 2, 3]
rotate([1, 2, 3], 6)           # → [1, 2, 3]
```

💡 `k = k % len(items)` нормализует. Потом: `items[-k:] + items[:-k]`.

---

### `deduplicate(items)`

Удаляет дубликаты, сохраняя **порядок первого вхождения**.

```python
deduplicate([1, 2, 1, 3, 2, 4])    # → [1, 2, 3, 4]
deduplicate([1, 1, 1])             # → [1]
deduplicate([])                    # → []
```

💡 Множество `seen` — добавляй в результат только если элемента ещё нет в `seen`.

---

### `zip_lists(a, b)`

Соединяет два списка в список пар. Останавливается на длине более короткого.

```python
zip_lists([1, 2, 3], ['a', 'b', 'c'])    # → [(1, 'a'), (2, 'b'), (3, 'c')]
zip_lists([1, 2], ['a', 'b', 'c'])       # → [(1, 'a'), (2, 'b')]
zip_lists([], [1, 2])                    # → []
```

💡 `range(min(len(a), len(b)))`.

---

### `unzip(pairs)`

Разбивает список пар на два отдельных списка.

```python
unzip([(1, 'a'), (2, 'b'), (3, 'c')])    # → ([1, 2, 3], ['a', 'b', 'c'])
unzip([])                                 # → ([], [])
```

💡 Два списка, наполняй в одном цикле: `firsts.append(pair[0])`, `seconds.append(pair[1])`.

---

## Часть 2: `comprehension.py`

> **Требование:** каждая функция — **одна строка** с comprehension. Проверяется автоматически.

### `evens_only(items)`
```python
evens_only([1, 2, 3, 4, 5, 6])    # → [2, 4, 6]
```
💡 `[x for x in items if ...]`

### `long_words(words, min_len)`
Слова **строго длиннее** `min_len` символов.
```python
long_words(["hi", "hello", "hey", "world"], 3)    # → ['hello', 'world']
```

### `pairs(n)`
Все пары `(i, j)` где `i < j`, оба из `range(n)`.
```python
pairs(4)    # → [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
```
💡 `[(i, j) for i in range(n) for j in range(n) if ...]`

### `unique_chars(s)`
Уникальные символы строки — **set comprehension**.
```python
unique_chars("banana")    # → {'b', 'a', 'n'}
```

### `word_lengths(words)`
Словарь `{слово: длина}` — **dict comprehension**.
```python
word_lengths(["hi", "hello"])    # → {'hi': 2, 'hello': 5}
```

### `transpose(matrix)`
```python
transpose([[1, 2, 3], [4, 5, 6]])    # → [[1, 4], [2, 5], [3, 6]]
```
💡 `[[row[i] for row in matrix] for i in range(len(matrix[0]))]`

### `group_by(f, items)`
Группирует по значению `f(x)`. Возвращает `{ключ: [элементы]}`.
```python
group_by(lambda x: x % 2, [1, 2, 3, 4, 5])    # → {1: [1, 3, 5], 0: [2, 4]}
```

### `all_triples(n)`
Все тройки `(i, j, k)` где `i < j < k` — тройная вложенность.
```python
all_triples(4)    # → [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
```

### `matrix_from_flat(flat, cols)`
Плоский список → матрица с `cols` столбцами.
```python
matrix_from_flat([1,2,3,4,5,6], 3)    # → [[1,2,3],[4,5,6]]
```
💡 `[flat[i*cols:(i+1)*cols] for i in range(len(flat)//cols)]`

---

## Часть 3 (продвинуто): `interval.py`

Абстракция интервала через конструктор и селекторы.

```python
i = interval(2, 5)
lower(i)   # → 2
upper(i)   # → 5
width(i)   # → 3
contains(i, 3)                        # → True
contains(i, 6)                        # → False
overlaps(interval(1, 4), interval(3, 7))    # → True
overlaps(interval(1, 3), interval(4, 7))    # → False
intersection(interval(1, 4), interval(3, 7))    # → interval(3, 4)
intersection(interval(1, 3), interval(4, 7))    # → None
```

> `width`, `contains`, `overlaps`, `intersection` — только через `lower`/`upper`. Не писать `i[0]` напрямую.

💡 *`overlaps`:* не пересекаются если `upper(i1) < lower(i2)` или наоборот.

---

## Часть 4 (продвинуто): `rational.py`

```python
half = rational(1, 2)
third = rational(1, 3)
print_rational(add_rational(half, third))     # → 5/6
print_rational(add_rational(third, third))    # → 2/3  (не 6/9!)
equal_rational(rational(2, 4), rational(1, 2))    # → True
```

> `add_rational`, `mul_rational`, `equal_rational` — только через `rational`, `numer`, `denom`.

💡 Формула сложения: `(n1*d2 + n2*d1) / (d1*d2)`. Конструктор сокращает через `gcd`.

---

## Как сдать

1. Форкни репозиторий
2. Реализуй функции
3. `pytest tests/ -v`
4. Commit и push — GitHub автоматически прогонит тесты
