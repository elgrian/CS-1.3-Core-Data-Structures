#!python

def pattern_empty(text, index_l, which):
    
    if which == 'contains':
        return True
        
    elif which == 'find_index':
        return 0
        
    elif which == 'find_all_indexes':
        for i in range(len(text)):
            index_l.append(i)
        return index_l


def pattern_true(index, which):
    
    if which == 'contains':
        return True
        
    elif which == 'find_index':
        return index


def pattern_false(which):
    
    if which == 'contains':
        return False
        
    elif which == 'find_index':
        return None


def string_master_func(text, pattern, which):
    index_l = []
    strings = ''
    if pattern == '':
        return pattern_empty(text, index_l, which)

    # Go through the text based on the length of the pattern
    for i in range(len(text) - len(pattern) + 1):
        # Go through all the characters that the pattern has
        for n in range(i, len(pattern) + i):
            # ADDs the characters to strings
            strings += text[n]
        # IF pattern is the same as strings
        if pattern == strings:
            if which == 'find_all_indexes':
                index_l.append(i)
                
            else:
                return pattern_true(i, which)
        # If not found, reset strings and empty it
        strings = ''

    if which == 'find_all_indexes':
        return index_l
    else:
        return pattern_false(which)


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    which = 'contains'
    return string_master_func(text, pattern, which)


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    which = 'find_index'
    return string_master_func(text, pattern, which)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    which = 'find_all_indexes'
    return string_master_func(text, pattern, which)


    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignores the script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
        
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()