# Math Cheatsheet

Here's a cheatsheet giving a summary about everything you need to know to code the wright functions.

# Online Courses

- If you wish to learn more about 'operators' in python you can either read this [article](https://www.programiz.com/python-programming/operators#what) or look at this [video](https://youtu.be/xTmEqNRr9T4).

- If you wish to learn more about 'lists' in python you can either read this [article](https://www.programiz.com/python-programming/list#create) or look at this [video](https://youtu.be/hANUgg72TDc).

# Kori's Courses

## my_square()

- As for many other programming languages, it is possible to do operations in python.

```
1 + 5 # '+' is a simple addition
>>> 6

-6 # '-a' A simple negation
>>> -6

5 - 1 # '-' is a simple substraction
>>> 4

5 * 3 # '*' is a simple multiplication
>>> 15

1 / 4 # '/' is a simple division, the result always has type float.
>>> 0.25

4 % 2 # '%' give the remainder when a is divided by b
>>> 0
```

## my_power()

- Unlike many programming languages Python does have some special operators you can use to do more complex operations.
```
5 // 2 # '//' is a simple division except the fact that the result is rounded up the next smallest whole number
>>> 2

2 ** 4 # '**' raise a to the power of b
>>> 16
```

## my_factorial()

- The factorial of x (noted x!) is the product of all integers less than or equal to x (ie. 5! = 1 * 2 * 3 * 4 * 5 = 120). For a more mathematical approach please check [Wikipedia](https://en.wikipedia.org/wiki/Factorial).

- There is 2 interisting approaches here:
    - An [iterative](https://en.wikipedia.org/wiki/Iteration) one using this pseudo-code.
    ```
    define factorial(n):
        f := 1
        for i := 1, 2, 3, ... n:
            f := f × i
        return f
    ```
    - A [recursive](https://en.wikipedia.org/wiki/Recursion_(computer_science)) one using this pseudo-code.
    ```
    define factorial(n):
        if n = 0
            return 1
        return n × factorial(n − 1)
    ```

## my_max()
- Lists can be traveled element by element.
    ```
    for element in [1, 2 ,3]:
        print(element)
    >>> 1
    >>> 2
    >>> 3
    ```

- Lists can be traveled index by index. In python indexes begin at 0 and finish at (n - 1), n being the number of elements in the list (ie. l = [1, 2, 3] have 3 elements so the last element can be refered as l[2] because 3 - 1 = 2).
    ```
    numbers = [1, 2, 3]
    for index in range(len(numbers) - 1):
        print(numbers[index])
    ```