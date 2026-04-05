def count_item(items, value):
    """Считает, сколько раз value встречается в списке."""
    count = 0
    for i in items:
        if i == value:
            count +=1 
    return count

def reverse_list(items):
    """Возвращает новый список в обратном порядке."""
    return items[::-1]

def flatten_once(nested):
    return [item for i in nested for item in i]


def chunk(items, n):
    """Разбивает список на куски по n элементов.
    Последний кусок может быть короче.
    """
    its = []
    if not items:
        return []
    for i in range(0,len(items), n):
        its.append(items[i:i+n])
    return its
def interleave(a, b):
    """Чередует элементы двух списков.
    Если списки разной длины — остаток более длинного добавляется в конец.
    """
    ist = []
    
    min_len = min(len(a), len(b))
    
    for i in range(min_len):
        ist.append(a[i])
        ist.append(b[i])
    
    ist.extend(a[min_len:])
    ist.extend(b[min_len:])
    
    return ist

def run_length_encode(items):
    ist = []
    
    if not items:
        return []
    
    current = items[0]
    count = 1

    for item in items[1:]:
        if item == current:
            count += 1
        else:
            ist.append((count, current))
            current = item
            count = 1

    ist.append((count, current))
    return ist

def rotate(items, k):
    """Сдвигает список вправо на k позиций.
    Отрицательный k — сдвиг влево.
    """
    if not items:
        return []
    k = k % len(items)
    return items[-k:] + items[:-k]

def deduplicate(items):
    """Удаляет дубликаты, сохраняя порядок первого вхождения."""
    lst = []
    for i in items:
        if i not in lst:
            lst.append(i)
    return lst

def zip_lists(a, b):
    """Соединяет два списка в список пар. Без использования zip()."""
    ist = []
    for i in range(min(len(a), len(b))):
        ist.append((a[i],b[i]))
    return ist


def unzip(pairs):
    """Разбивает список пар на два списка."""
    ist = []
    item = []
    for i,y in pairs:
        ist.append(i)
        item.append(y)
    return (ist,item)