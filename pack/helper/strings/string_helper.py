def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

def capitalize_string(s):
    return s.capitalize()

def title_case(s):
    return s.title()

def reverse_string(s):
    return s[::-1]

def string_length(s):
    return len(s)

def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

def remove_spaces(s):
    return s.replace(" ", "")

def is_palindrome(s):
    return s == s[::-1]

def find_substring(s, sub):
    return s.find(sub)