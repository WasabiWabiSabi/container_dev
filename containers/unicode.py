import unicodedata


class NormalizedStr:
    '''
    By default, Python's str type stores any valid unicode string.
    This can result in unintuitive behavior.
    For example:

    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False

    The two strings to the right of the in keyword above are equal *seman
    but not equal *representationally
    In particular, the first is in NFC form, and the second is in NFD form.
    The purpose of this class is to automatically normalize our strings for u
    making foreign languages "just work" a little bit easier.
    '''

    def __init__(self, text, normal_form='NFC'):
        self.normal = normal_form
        self.text = unicodedata.normalize(self.normal, text)

    def __repr__(self):
        '''
        The string returned by the __repr__ function should be valid python
        that can be substituted directly into the python interpreter to rept.
        '''
        return 'NormalizedStr(\'' + self.text + '\', \'' + self.normal + '\')'

    def __str__(self):
        '''
        This functions converts the NormalizedStr into a regular string objt.
        The output is similar, but not exactly the same, as the __repr__ fun
        '''
        return str(self.text)

    def __len__(self):
        '''
        Returns the length of the string.
        The expression `len(a)` desugars to a.__len__().
        '''
        return len(self.text)

    def __contains__(self, substr):
        normal_substr = unicodedata.normalize(self.normal, substr)
        return str(self.text).__contains__(str(normal_substr))

    def __getitem__(self, index):
        '''
        Returns the character at position `index`.
        The expression `a[b]` desugars to `a.__getitem__(b)`.
        '''
        indexable_list = list(self.text)
        return indexable_list[index]

    def lower(self):
        '''
        Returns a copy in the same normalized form, but lower case.
        '''
        return self.text.lower()

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''
        return self.text.upper()

    def __add__(self, b):
        '''
        Returns a copy of `self` with `b` appended to the end.
        The expression `a + b` gets desugared into `a.__add__(b)`.

        HINT
        The addition of two normalized strings is not guaranteed to stay
        Therefore, you must renormalize the strings after adding them t
        '''
        b_norm = unicodedata.normalize(self.normal, str(b))
        combined_self = unicodedata.normalize(self.normal, self.text + b_norm)
        return NormalizedStr(combined_self, self.normal)

    def __iter__(self):
        '''
        HINT:
        Recall that the __iter__ method returns a class, which is the iterat
        You'll need to define your own iterator class with the appropriate
        and return an instance of that class here.
        '''
        return NormIter(self.text)


class NormIter:

    def __init__(self, text):
        self.text = text
        self.count = 0

    def __next__(self):
        if self.count < len(self.text):
            self.count += 1
            return self.text[self.count - 1]
        else:
            raise StopIteration
