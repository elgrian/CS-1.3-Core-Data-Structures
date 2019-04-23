#!python
import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_alpha_characters is ascii_lowercase + ascii_uppercase


alpha_characters = frozenset(string.ascii_letters) # dictionary without values
def is_palindrome(text):
    """A string of alpha_characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    right = len(text) - 1 
    left = 0
    while left <= right: # goes through both sides of the text
        # ignores all of the special alpha_characters
        while text[left] not in alpha_characters:
            left += 1
        while text[right] not in alpha_characters:
            right -= 1
        # if the alpha_characters don't match up, then make bothlowercase
        if text[left].lower() != text[right].lower():
            # the lowercase alpha_characters did not match
            return False
        left += 1
        right -= 1
    return True # the word IS a palindrome

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    if left == None:
        left = 0
        right = len(text) - 1
    # finished going through the text
    if left >= right:
        return True
    # ignores all the special alpha_characters
    if text[left] not in alpha_characters:
        return is_palindrome_recursive(text, left + 1, right)
    if text[right] not in alpha_characters:
        return is_palindrome_recursive(text, left, right - 1)
    # found some alpha_characters that don't match up
    if text[left] != text[right]:
        if text[left].lower() != text[right].lower():
            return False
    return is_palindrome_recursive(text, left + 1, right - 1)
def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
