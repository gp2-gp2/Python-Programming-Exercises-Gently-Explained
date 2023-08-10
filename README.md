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

```bash
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz
```

Prerequisite concepts: modulo operator, end keyword argument for print(), for loops, range() with two arguments.

## Ex 6 "Ordinal Suffix"

Exercise Description

In English, ordinal numerals have suffixes such as the "th" in "30th" or "nd" in "2nd". Write an ordinalSuffix() function with an integer parameter named number and returns a string of the number with its ordinal suffix. For example, ordinalSuffix(42) should return the string '42nd'.
You may use Python’s str() function to convert the integer argument to a string. Python’s endswith() string method could be useful for this exercise, but to maintain the challenge in this exercise, don’t use it as part of your solution.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

```python
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
```

Prerequisite concepts: strings, in operator, slices, string concatenation.

## Ex 7 "ASCII Table"

Exercise Description

Write a printASCIITable() function that displays the ASCII number and its corresponding text character, from 32 to 126. (These are called the printable ASCII characters.)
Your solution is correct if calling printASCIITable() displays output that looks like the following:

```bash
32 
33 !
34 "
35 #
--more--
124 |
125 }
126 ~
```

Note that the character for ASCII value 32 is the space character, which is why it looks like nothing is next to 32 in the output.

Prerequisite concepts: for loops, range() with two arguments, chr().

## Ex 8 "Read Write File"

Exercise Description

You will write three functions for this exercise. First, write a writeToFile() function with two parameters for the filename of the file and the text to write into the file. Second, write an appendToFile() function, which is identical to writeToFile() except that the file opens in append mode instead of write mode. Finally, write a readFromFile() function with one parameter for the filename to open. This function returns the full text contents of the file as a string.
These Python instructions should generate the file and the assert statement checks that the content is correct:

```python
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
```

This code writes the text 'Hello!\n' and 'Goodbye!\n' to a file named greet.txt, then reads in this file’s content to verify it is correct. You can delete the greet.txt file after running these instructions program.

Prerequisite concepts: text file reading and writing.

## Ex 9 "Chess Square Color"

Exercise Description

A chess board has a checker-pattern of white and black tiles. In this program, you’ll determine a pattern to the color of the squares based on their column and row. This program challenges you to take a real-world object such as a chess board, determine the patterns behind its design, and translate that into Python code.

Write a getChessSquareColor() function that has parameters column and row. The function either returns 'black' or 'white' depending on the color at the specified column and row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and end at 7 like in Figure 9-1. If the arguments for column or row are outside the 0 to 7 range, the function returns a blank string.

Top left corner is white and has (0, 0) coordinates .

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

```python
assert getChessSquareColor(1, 1) == "white"
assert getChessSquareColor(2, 1) == "black"
assert getChessSquareColor(1, 2) == "black"
assert getChessSquareColor(8, 8) == "white"
assert getChessSquareColor(0, 8) == ""
assert getChessSquareColor(2, 9) == ""
```
