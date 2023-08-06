# Python-Programming-Exercises-Gently-Explained

Simple repo for keeping track of the exercises

## Ex 1 "Hello World"

Exercise Description

Write a program that, when run, greets the user by printing "Hello, world!" on the screen. Then it prints a message on the screen asking the user to enter their name. The program greets the user by name by printing the "Hello," followed by the user’s name.

Let’s use "Alice" as the example name. Your program’s output should look like this:

```bash
Hello, world!
What is your name?
Alice
Hello, Alice
```

Prerequisite concepts: print(), strings, string concatenation.

## Ex 2 "Temperature Conversion"

Exercise Description

Write a convertToFahrenheit() function with a degreesCelsius parameter. This function returns the number of this temperature in degrees Fahrenheit. Then write a function named convertToCelsius() with a degreesFahrenheit parameter and returns a number of this temperature in degrees Celsius.

Use these two formulas for converting between Celsius and Fahrenheit:

```python
Fahrenheit = Celsius × (9 / 5) + 32
Celsius = (Fahrenheit - 32) × (5 / 9)
```

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

```python
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
```

Rounding errors cause a slight discrepancy:

```python
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
```

Prerequisite concepts: math operators.

## Ex 3 "Odd & Even"

Exercise Description

Write two functions, isOdd() and isEven(), with a single numeric parameter named number. The isOdd() function returns True if number is odd and False if number is even. The isEven() function returns the True if number is even and False if number is odd. Both functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered an even number.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

```Python
assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False
```

Prerequisite concepts: modulo operator

## Ex 4 "Area and Volume"

Exercise Description

You will write four functions for this exercise. The functions area() and perimeter() have length and width parameters and the functions volume() and surfaceArea() have length, width, and height parameters. These functions return the area, perimeter, volume, and surface area, respectively.
The formulas for calculating area, perimeter, volume, and surface area are based on the length (L), width (W), and height (H) of the shape:
area = L × W
perimeter = L + W + L + W
volume = L × W × H
surface area = (L × W × 2) + (L × H × 2) + (W × H × 2)
Area is a two-dimensional measurement from multiplying length and width. Perimeter is the sum of all of the four one-dimensional lines around the rectangle. Volume is a three-dimensional measurement from multiplying length, width, and height. Surface area is the sum of all six of the two-dimensional areas around the cube. Each of these areas comes from multiplying two of the three length, width, or height dimensions.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

```python
assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340
```

## Ex 5 "Fizz Buzz"

Exercise Description

Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1 up to and including upTo, the function prints one of four things:
Prints 'FizzBuzz' if the number is divisible by 3 and 5.
Prints 'Fizz' if the number is only divisible by 3.
Prints 'Buzz' if the number is only divisible by 5.
Prints the number if the number is neither divisible by 3 nor 5.

Instead of printing each string or number on a separate line, print them without newlines. For example, your solution is correct if calling fizzBuzz(35) produces the following output:

1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz

Prerequisite concepts: modulo operator, end keyword argument for print(), for loops, range() with two arguments.
