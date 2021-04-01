def range(a, b=None, c=None):
    '''
    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    if b is None and c is None:
        i = 0
        count = 0
        while i <= (a - 1):
            yield count
            count += 1
            i += 1
    elif c is None:
        if b > a:
            count = a
            i = 0
            while i <= (b - a - 1):
                yield count
                count += 1
                i += 1
        else:
            pass
    else:
        count = a
        i = 0
        itr = abs(b - a) - 1
        if c < 0 and b > 0:
            base = c
        else:
            base = abs(c)
        while i <= itr / base:
            yield count
            i += 1
            count += c
