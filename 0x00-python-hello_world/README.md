# 0X00 Hello World - Python

# 0. Run Python file

> Write a Shell script that runs a Python script.

> The Python file name will be saved in the environment variable `$PYFILE`
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```

# 1. Run inline

> Write a Shell script that runs Python code.

> The Python code will be saved in the environment variable `$PYCODE`
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```

# 2. Hello, print

> Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

> Use the function `print`
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

# 3. Print integer

> Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

> You can find the source code here
> The output of the script should be:
> the number, followed by Battery street,
> followed by a new line
> You are not allowed to cast the variable number into a string
> Your code must be 3 lines long
> You have to use `f-strings` tips
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```

# 4. Print float

* Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

> You can find the source code here
>The output of the program should be:
> Float:, followed by the float with only 2 digits
> followed by a new line
> You are not allowed to cast number to string
> You have to use f-strings
```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```

# 5. Print string

> You can find the source code here
> The output of the program should be:
> 3 times the value of str
> followed by a new line
> followed by the 9 first characters of str
> followed by a new line
> You are not allowed to use any loops or conditional statement
> Your program should be maximum 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
```
# 6. Play with strings

> You can find the source code here
> You are not allowed to use any loops or conditional statements.
> You have to use the variables str1 and str2 in your new line of code
> Your program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
```

# 7. Copy - Cut - Paste

> You can find the source code here
> You are not allowed to use any loops or conditional statements
> Your program should be exactly 8 lines long
> word_first_3 should contain the first 3 letters of the variable word
> word_last_2 should contain the last 2 letters of the variable word
> middle_word should contain the value of the variable word without the first and last letters
```
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 
```

# 8.Create a new sentence
> You can find the source code here
> You are not allowed to use any loops or conditional statements
> Your program should be exactly 5 lines long
> You are not allowed to create new variables
> You are not allowed to use string literals
```
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
```

# 9. Easter Egg

> Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

> Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
```
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$9. Easter Egg
```

# 11. Hello, write

> Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

> Use the function write from the `sys module`
> You are not allowed to use print
> Your script should print to stderr
> Your script should exit with the status code 1
```
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ 
```
