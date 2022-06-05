#!/bin/python3

###################################
# Import stdlib functions
from inspect import *

# Import functions from src/string/
from src.string import *
from src.math import *

# Define useful functions

def is_func_written(func) -> bool:
    """
    Returns True if the function has been written.
    """
    a = getsource(func).split('\n')
    return a[len(a) - 2] != '    ...'

#####################
# Math functions
#####################

# -> my_square check
if is_func_written(my_square):
    print("🧪 My_square: Testing.")
    assert(my_square(2) == 4)
    assert(my_square(3) == 9)
    assert(my_square(4) == 16)
    assert(my_square(5) == 25)
    assert(my_square(6) == 36)
    assert(my_square(7) == 49)
    assert(my_square(8) == 64)
    assert(my_square(9) == 81)
    assert(my_square(10) == 100)
    assert(my_square(11) == 121)
    assert(my_square(12) == 144)
    assert(my_square(13) == 169)
    print("✨ My_square: All Good!\n")
else:
    print("🧬 My_square: Not written yet.\n")

if is_func_written(my_power):
    print("🧪 My_power: Testing.")
    assert(my_power(2, 3) == 8)
    assert(my_power(2, 0) == 1)
    assert(my_power(2, 1) == 2)
    assert(my_power(2, 4) == 16)
    assert(my_power(2, 5) == 32)
    assert(my_power(2, 6) == 64)
    assert(my_power(3, 3) == 27)
    assert(my_power(3, 0) == 1)
    assert(my_power(3, 1) == 3)
    assert(my_power(3, 2) == 9)
    assert(my_power(3, 4) == 81)
    assert(my_power(3, 5) == 243)
    assert(my_power(10, 3) == 1000)
    assert(my_power(10, 0) == 1)
    assert(my_power(10, 1) == 10)
    assert(my_power(10, 2) == 100)
    print("✨ My_power: All Good!\n")
else:
    print("🧬 My_power: Not written yet.\n")

if is_func_written(my_factorial):
    print("🧪 My_factorial: Testing.")
    assert(my_factorial(0) == 1)
    assert(my_factorial(1) == 1)
    assert(my_factorial(2) == 2)
    assert(my_factorial(3) == 6)
    assert(my_factorial(4) == 24)
    assert(my_factorial(5) == 120)
    assert(my_factorial(6) == 720)
    assert(my_factorial(7) == 5040)
    assert(my_factorial(8) == 40320)
    assert(my_factorial(9) == 362880)
    assert(my_factorial(10) == 3628800)
    assert(my_factorial(11) == 39916800)
    assert(my_factorial(12) == 479001600)
    assert(my_factorial(13) == 6227020800)
    print("✨ My_factorial: All Good!\n")
else:
    print("🧬 My_factorial: Not written yet.\n")

if is_func_written(my_max):
    print("🧪 My_max: Testing.")
    assert(my_max([1, 2, 3]) == 3)
    assert(my_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10)
    assert(my_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20)
    assert(my_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 30)
    assert(my_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 40)
    assert(my_max([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40]) == -1)
    assert(my_max([0, 2, -1, 10, 43, 12]) == 43)
    print("✨ My_max: All Good!\n")
else:
    print("🧬 My_max: Not written yet.\n")

#####################
# String functions
#####################

# -> spell_word check
if is_func_written(spell_word):
    print("🧪 Spell_word: Testing.")
    assert(spell_word("bonjour") == ["b","o","n","j","o","u","r"])
    assert(spell_word("Bonjour") == ["b","o","n","j","o","u","r"])
    assert(spell_word("bonjour ") == [])
    assert(spell_word("bonjour.") == [])
    assert(spell_word("au revoir") == [])
    assert(spell_word("bye") == ["b", "y", "e"])
    assert(spell_word("arive") == ["a", "r", "i", "v", "e"])
    assert(spell_word("derci") == ["d", "e", "r", "c", "i"])
    assert(spell_word("Sortie") == ["s","o","r","t","i","e"])
    assert(spell_word("sortie") == ["s","o","r","t","i","e"])
    assert(spell_word("sortie ") == [])
    assert(spell_word("sortie.") == [])
    print("✨ Spell_word: All Good!\n")
else:
    print("🧬 Spell_word: Not written yet.\n")

# -> histogram check
if is_func_written(histogram):
    print("🧪 Histogram: Testing.")
    assert(histogram("bonjour") == {"b": 1, "o": 2, "n": 1, "j": 1, "u": 1, "r": 1})
    assert(histogram("mexicain") == {"m": 1, "e": 1, "x": 1, "i": 2, "c": 1, "a": 1, "n": 1})
    assert(histogram("zemmour") == {"z": 1, "e": 1, "m": 2, "o": 1, "u": 1, "r": 1})
    assert(histogram("volleyball") == {"v": 1, "o": 1, "l": 4, "e": 1, "y": 1, "b": 1, "a": 1})
    assert(histogram("") == {})
    assert(histogram("histogram") == {"h": 1, "i": 1, "s": 1, "t": 1, "o": 1, "g": 1, "r": 1, "a": 1, "m": 1})
    assert(histogram("histogramm") == {"h": 1, "i": 1, "s": 1, "t": 1, "o": 1, "g": 1, "r": 1, "a": 1, "m": 2})
    assert(histogram("histogrammm") == {"h": 1, "i": 1, "s": 1, "t": 1, "o": 1, "g": 1, "r": 1, "a": 1, "m": 3})
    assert(histogram("histogrammmm") == {"h": 1, "i": 1, "s": 1, "t": 1, "o": 1, "g": 1, "r": 1, "a": 1, "m": 4})
    assert(histogram("histogrammmmm") == {"h": 1, "i": 1, "s": 1, "t": 1, "o": 1, "g": 1, "r": 1, "a": 1, "m": 5})
    assert(histogram("au revoir") == {})
    print("✨ Histogram: All Good!\n")
else:
    print("🧬 Histogram: Not written yet.\n")

# -> palindrome check
if is_func_written(palindrome):
    print("🧪 Palindrome: Testing.")
    assert(palindrome("bonjour") == False)
    assert(palindrome("Bonjour") == False)
    assert(palindrome("bonjour ") == False)
    assert(palindrome("bonjour.") == False)
    assert(palindrome("au revoir") == False)
    assert(palindrome("bye") == False)
    assert(palindrome("arive") == False)
    assert(palindrome("kayak") == True)
    assert(palindrome("kayak ") == False)
    assert(palindrome("kayak.") == False)
    assert(palindrome("Kayak") == True)
    assert(palindrome("kayak!") == False)
    assert(palindrome("kayak a kayak") == True)
    assert(palindrome("kayak a kayak ") == False)
    assert(palindrome(".kayak a kayak.") == True)
    print("✨ Palindrome: All Good!\n")
else:
    print("🧬 Palindrome: Not written yet.\n")
