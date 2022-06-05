# String Cheatsheet

Here's a cheatsheet giving a summary about everything you need to know to code the wright functions.

# Online Courses

- If you wish to learn more about 'strings' in python you can either read this [article](https://www.programiz.com/python-programming/string#what) or look at this [video](https://youtu.be/GQywwPUrsgA).

- If you wish to learn more about 'dictionaries' in python you can either read this [article](https://www.programiz.com/python-programming/string#what) or look at this [video](https://youtu.be/_4wOvc-vt4k).

# Kori's Courses

## spell_word()

- You can itterate throught strings as you itterate throught lists.
```
for letter in "bonjour":
    print(letter)

>>> b
>>> o
>>> n
>>> j
>>> o
>>> u
>>> r
```

## histogram()

- You can create an empty dictionnary by specifying '{ }' instead of '[ ]' that is used for lists.

```
dictionnaire = {}
```

- Dictionnaries can store a 'key' and a 'value'.

```
kda = {'kill': 13, 'death': 7, 'assist': 27}
```

- Like the elements of a list, elements inside a dictionnary can be reffered by giving the dictionnary but instead of the index we will use the 'key'.

```
print(kda[kill])
>>> 13
```

- Like a for lists, python is smart enough to allocate or re-allocate memory when needed so you can force an 'key: value' pair to be created or changed IF IT WAS DEFINED EMPTY (ie. dict = {}).

```
kda = {'kill': 13, 'death': 7}
print(kda)

>>> {'kill': 13, 'death': 7}

kda['assist'] = 27
print(kda)

>>> {'kill': 13, 'death': 7, 'assist': 27}
```

## palindrome()

- Palindromes are words or sentences that can be read from both ways (ie. 'KAYAK' reversed is 'KAYAK' but 'HELLO' reversed is 'OLLEH').

- The only way to know if a string is a palindrom is to check if the string and the reversed string are equal. You have 2 possibilities:
    - Create a new string, loop through the argument from the last letter to the first one and then add each letter to the string. Afterwards, check if your original string is equal to the new one.

    - Check if a letter is equal to it's opposite (ie. We have 'Kayak', let's check if word[0] == word[4], word[1] == word[3], and if word[2] == word[2]).
