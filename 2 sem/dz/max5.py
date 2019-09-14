import random

numbers = [random.randint(5,15) for x in range(20)]

def max_sequence(seq,n=5): # n - длина подспиков
    
    """
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.

    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]

    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    """

    subs = [seq[x:x+n] for x in range(len(numbers)-n+1)]

    totalsubs = [sum(subs[x]) for x in range(len(subs))]

    totalsubs.index(max(totalsubs))

    return subs[totalsubs.index(max(totalsubs))]

print(max_sequence(numbers))
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

