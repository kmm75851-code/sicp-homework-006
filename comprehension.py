def evens_only(items):
    """Только чётные числа из списка."""
    even_numbers = [i for i in items if i // 2 == 0]
    return even_numbers

def long_words(words, min_len):
    """Слова длиннее min_len символов."""
    min3 = [i for i in words if len(i) > min_len]
    return min3
    

def pairs(n):
    """Все пары (i, j), где i < j, оба из range(n)."""
    j_more = [(i, j) for i in range(n) for j in range(n) if i < j]

def unique_chars(s):
    """Уникальные символы строки — через set comprehension."""
    return {i for i in s}

def word_lengths(words):
    """Словарь {слово: длина} — через dict comprehension."""
    return {i: len(i) for i in words}

def transpose(matrix):
    """Транспонирует матрицу (список списков) через nested comprehension."""
    return [[f] for i in matrix for f in i ]
    
transpose([[1, 2, 3], [4, 5, 6]])    # → [[1, 4], [2, 5], [3, 6]]
def group_by(f, items):
    """Группирует элементы по значению f(x) через dict comprehension.
    Возвращает словарь {ключ: [элементы с таким ключом]}.
    """
    return{i:[f(x)]for i in items}

def all_triples(n):
    """Все тройки (i, j, k), где i < j < k, все из range(n).
    Тройная вложенность.
    """
    k_more = [(i, j, k) for i in range(n) for j in range(n) for k in range(n)if i < j  < k]
    return k_more

def matrix_from_flat(flat, cols):
    """Превращает плоский список в матрицу с cols столбцами.
    Из плоского — во вложенное.
    """
    return [flat[i:i+cols] for i in range(0, len(flat), cols)]
   
    
