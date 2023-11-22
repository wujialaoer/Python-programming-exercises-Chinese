import math
import re
import timeit
from functools import reduce
from itertools import permutations
from operator import itemgetter
from random import shuffle

"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
 between 2000 and 3200 (both included).The numbers obtained should be printed in a
 comma-separated sequence on a single line.

 编写一个程序，找出 2000 到 3200（包括在内）之间能被 7 整除但不是 5 的倍数的数。得到的数字应以逗号分隔的序列形式打印在同一行上。
"""


def get_nums():
    l = []

    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            l.append(str(i))
    print(','.join(l))


"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320  

计算给定数字的阶乘的程序。结果应以逗号分隔的形式在同一行打印。
假设向程序提供以下输入：8 然后，输出应为：40320
"""


def fact(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    return reduce(lambda x, y: x * y, [i for i in range(1, n + 1)])
    # return reduce(lambda x, y: x * y, [i for i in range(1, n + 1)]) if n > 0 else 1
    # if n == 0:
    #     return 1
    # return n * fact(n - 1)


"""
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

给定一个整数 n，编写一个程序，生成一个包含（i，i*i）的字典，其中 i 是一个介于 1 和 n（均包含）之间的整数。然后程序应打印该字典。
假设以下输入供应给程序：
8 那么，输出应该是：
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""


def make_dict(n):
    d = {}
    if n < 0:
        return -1
    print({i: i * i for i in range(1, n + 1)})
    # for i in range(1, n + 1):
    #     d[i] = i * i
    # print(d)


"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

编写一个程序，从控制台接受一系列由逗号分隔的数字，并生成一个包含所有数字的列表和一个元组。
假设以下输入供应给程序：
34,67,55,33,12,98
那么，输出应该是：
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""


def handle_type(st):
    print(st)
    print(st.split(','))
    print(tuple(st.split(',')))


"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

定义一个类，至少包含两个方法：
getString：从控制台输入获取一个字符串
printString：将字符串转换为大写并打印。
同时，请包括一个简单的测试函数来测试类的方法。
"""


class StrHandle(object):
    def __init__(self):
        self.ipt = ''

    def get_string(self):
        self.ipt = input('请输入一个字符串： ： ')
        return self.ipt

    def print_string(self):
        return print('大写字符串 ', self.ipt.upper())


def test_string():
    sh = StrHandle()
    sh.get_string()
    sh.print_string()


"""
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24


编写一个程序，根据给定公式计算并打印值：
Q = [(2 * C * D) / H] 的平方根
以下分别是 C 和 H 的固定值：
C 为 50。H 为 30。
D 是变量，其值应输入到程序中。
示例
假设以下是一个逗号分隔的输入序列：
100,150,180
程序的输出应为：
18，22，24
"""


def calculate_q(st):
    l = st.split(',')
    for i in l:
        print(round((2 * 50 * float(i) / 30) ** 0.5))


"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

编写一个程序，接收两个数字 X、Y 作为输入，生成一个二维数组。数组中每个元素的值应为 i-th 行和 j-th 列的乘积。
注意：i 从 0 到 X-1；j 从 0 到 Y-1。
示例
假设以下输入传递给程序：
3,5
那么程序的输出应如下所示：
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

"""


def li(row_num, cow_num):
    mul = [[0 for i in range(cow_num)] for j in range(row_num)]
    for row in range(row_num):
        for col in range(cow_num):
            mul[row][col] = row * col

    print(mul)


"""
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

编写一个程序，接受以逗号分隔的单词序列作为输入，并将排序后的单词以逗号分隔的序列打印出来。
假设以下输入供应给程序：
without,hello,bag,world
那么，输出应该是：
bag,hello,without,world
"""


def sort_input(st):
    l = [i for i in st.split(',')]
    l.sort()
    print(','.join(l))


"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

编写一个程序，接受一行行的输入，并将每行的所有字符转换为大写后打印出来。
假设以下输入供应给程序：
Hello world
Practice makes perfect
那么，输出应该是：
HELLO WORLD
PRACTICE MAKES PERFECT
"""


def str_upper():
    lines = []
    while 1:
        i = input('input:   ')
        if i:
            lines.append(i.upper())
        else:
            break
    for i in lines:
        print(i)


"""
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world


编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复单词后按字母数字顺序打印单词。
假设以下输入供应给程序：
hello world and practice makes perfect and hello world again
那么输出应该是：
again and hello makes perfect practice world
"""


def sort_diff(st):
    # l = list(set(st.split(' ')))
    # l.sort()
    # print(l)
    print(' '.join(sorted(list(set(st.split(' '))))))


"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

编写一个程序，接受一系列逗号分隔的 4 位二进制数作为输入，然后检查它们是否可以被 5 整除。将被 5 整除的数字以逗号分隔的序列打印出来。
示例：
0100,0011,1010,1001
输出应为：
1010
"""


def num_divisible(input_data):
    # input_data = input("请输入一系列 4 位二进制数，用逗号分隔：")
    value = []
    items = [i for i in input_data.split(',')]
    for p in items:
        intp = int(p, 2)
        print(intp)
        if not intp % 5:
            value.append(p)

    print(','.join(value))


"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.The numbers obtained should be printed 
in a comma-separated sequence on a single line.

写一个程序，找到1000到3000之间的所有这些数字（都包括在内），这个数字的每个数字都是偶数。
获得的数字应以逗号分隔的顺序打印在一行上。
"""


def get_even_nums():
    digits = [i for i in range(0, 10) if i % 2 == 0]
    nums = []
    for i in range(1000, 3001):
        current = str(i)
        if all(int(d) in digits for d in current):
            nums.append(str(i))
    print(nums)


"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3


写一个程序，接受一个句子并计算其中字母和数字的数量。
假设以下输入数据供应给程序：
hello world! 123
那么，输出应该是：
LETTERS 10
DIGITS 3
"""


def get_totals(st):
    LETTERS = DIGITS = 0

    for i in st:
        if i.isalpha():
            LETTERS += 1
        elif i.isdigit():
            DIGITS += 1

    print('LETTERS   ', LETTERS, '\n', 'DIGITS   ', DIGITS)


"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

写一个程序，接受一个句子并计算其中大写字母和 lowercase 字母的数量。
假设以下输入数据供应给程序：
Hello world!
那么，输出应该是：
UPPER CASE 1
LOWER CASE 9
"""


def get_upper_lower_nums(st: str):
    upper = lower = 0
    for i in st:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1

    print('UPPER CASE   ', upper, '\n', 'LOWER CASE   ', lower)


"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106   

计算 a+aa+aaa+aaaa 的值，其中 a 的值是给定的数字。
假设以下输入数据供应给程序：
9 那么，输出应该是：
11106
"""


def sum_nums(n):
    print(n + n * 11 + n * 111 + n * 1111)


"""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

使用列表推导式获取列表中的每个奇数。该列表由逗号分隔的数字序列输入。
假设向程序提供以下输入：
1,2,3,4,5,6,7,8,9
那么，输出应该是：
1,3,5,7,9

"""


def get_odd(st: str):
    print(','.join([i for i in st.split(',') if int(i) % 2 != 0]))


"""
Write a program that computes the net amount of a bank account based a transaction log from console input.
 The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

编写一个程序，根据控制台输入的交易日志计算银行账户的净额。事务日志格式如下所示：
D 100
W 200
D表示存款，W表示提款。
假设向程序提供以下输入：
D 300
D 300
W 200
D 100
那么，输出应该是：
500
"""


def get_money():
    balance = 0
    while True:
        inpt = input("input  :")
        if not inpt:
            break
        values = inpt.split(' ')
        if values[0] == 'D':
            balance += int(values[1])
        elif values[0] == 'W':
            balance -= int(values[1])
        else:
            break
    print(balance)


"""
A website requires the users to input username and password to register.
 Write a program to check the validity of password input by users.
Following are the criteria for checking the password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
   Your program should accept a sequence of comma separated passwords and will 
   check them according to the above criteria.
    Passwords that match the criteria are to be printed, each separated by a comma.
   Example
   If the following passwords are given as input to the program:
   ABd1234@1,a F1#,2w3E*,2We3345
   Then, the output of the program should be:
   ABd1234@1


网站要求用户输入用户名和密码才能注册。编写一个程序来检查用户输入的密码的有效性。
以下是检查密码的标准：
1.[a-z]之间至少有一个字母
2.[0-9]之间至少有1个数字
3.[A-Z]之间至少有一个字母
4.[$#@]中至少有1个字符
5.交易密码最小长度：6
6、交易密码最大长度：12
您的程序应接受逗号分隔的密码序列，并将根据上述标准进行检查。将打印符合条件的密码，每个密码用逗号分隔。


如果将以下密码作为程序的输入：
ABd1234@1，一个F1#，2w3E*，2We3345
然后，程序的输出应该是：
ABd1234@1
"""


def check_pwd(pwd: str):
    value = []
    for p in pwd.split(','):

        if len(p) < 6 or len(p) > 12:
            continue

        if not re.search('[0-9]', p):
            continue
        elif not re.search('[a-z]', p):
            continue
        elif not re.search('[A-Z]', p):
            continue
        elif not re.search('[$#@]', p):
            continue
        elif re.search('\s', p):
            continue

        value.append(p)
    print(','.join(value))


"""
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, 
age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

您需要编写一个程序来按升序对（name，age，height）元组进行排序，其中name是字符串，age和height是数字。元组是通过控制台输入的。排序标准为：
1：按名称排序；
2：然后根据年龄排序；
3：然后按分数排序。
优先级是姓名>年龄>分数。
如果将以下元组作为程序的输入：
汤姆，19,80
约翰，20,90
Jony，17,91
Jony，17,93
Json，21,85
然后，程序的输出应该是：
[（'John'，'20'，'90'），（'Jony'，'17'，'91'），（'Jony'，'17'，'93'），[Json'，'21'，'85']，（'Tom'，'19'，'80'）]

"""


def sort_tuple():
    l = [
        'Tom, 19, 80',
        'John, 20, 90',
        'Jony, 17, 91',
        'Jony, 17, 93',
        'Json, 21, 85'
    ]
    t = []
    for i in l:
        t.append(tuple(i.split(',')))
    print(sorted(t, key=itemgetter(0, 1, 2)))


"""
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.


用生成器定义一个类，该生成器可以迭代给定范围0和n之间的可被7整除的数字。

"""


class DivisibleBySeven(object):
    def __init__(self, n):
        self.count = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            raise StopIteration
        else:
            self.count += 1
            return self.count if self.count % 7 == 0 else None

    # def __len__(self):
    #     return self.n // 7


"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN,
 LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position
 after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

机器人在从原点（0,0）开始的平面中移动。机器人可以按给定的步骤向上、向下、向左和向右移动。机器人运动轨迹如下所示：
UP 5
DOWN 3
LEFT 3
RIGHT 2
方向后面的数字是步长。请编写一个程序来计算一系列移动和原点后与当前位置的距离。如果距离是一个浮点值，那么只需打印最近的整数。
示例：
如果将以下元组作为程序的输入：
UP 5
DOWN 3
LEFT 3
RIGHT 2
然后，程序的输出应该是：
2
"""


def get_move_sqrt():
    pos = [0, 0]
    while True:
        ipt = input('input   :')
        if not ipt:
            break
        movement = ipt.split(' ')
        if movement[0] == 'UP':
            pos[0] += int(movement[1])
        elif movement[0] == 'DOWN':
            pos[0] -= int(movement[1])
        elif movement[0] == 'LEFT':
            pos[1] -= int(movement[1])
        elif movement[0] == 'RIGHT':
            pos[1] += int(movement[1])
    print(int(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2))))


"""
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1


编写一个程序来计算输入单词的频率。输出应该在对键进行字母数字排序后输出。
假设向程序提供以下输入：
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
那么，输出应该是：
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1



"""


def get_key_count(st: str):
    d = {}
    for i in st.split(' '):
        d[i] = d.get(i, 0) + 1
    for k, v in sorted(d.items(), key=lambda x: x[0]):
        print(f"{k}: {v}")


"""


### Question 23

level 1

Question:
Write a method which can calculate square value of number

Hints:
Using the ** operator

Solution:

```python
def square(num):
    return num ** 2

print(square(2))
print(square(3))
```
```
###问题23
级别1
问题：
写一个可以计算数字平方值的方法
提示：
使用**运算符
解决方案：
```python
def平方（num）：
返回编号**2
打印（方形（2））
打印（正方形（3））
```



### Question 24

Level 1

Question:

Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function
Hints:
The built-in document method is __doc__

Solution:

```python
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print(square(2))
print(square.__doc__)
```

###问题24
级别1
问题：
Python有许多内置函数，如果您不知道如何使用它，您可以在线阅读文档或查找一些书籍。但是Python对于每个内置函数都有一个内置的文档函数。
请编写一个程序来打印一些Python内置函数文档，如abs（）、int（）、raw_input（）
并为您自己的功能添加文档
提示：
内置的文档方法是__doc__
解决方案：
```python
打印（abs.__doc__）
打印（int.__doc__）
打印（输入__doc__）
def平方（num）：
''返回输入数字的平方值。
输入数字必须是整数。
“”
返回编号**2
打印（方形（2））
打印（方形__doc__）
```





### Question 25

Level 1

Question:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define a instance parameter, need add it in __init__ method
You can init a object with construct parameter or set the value later

Solution:

```python
class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))
```

###问题25
级别1
问题：
定义一个类，该类具有类参数并具有相同的实例参数。
提示：
定义一个实例参数，需要在__init__方法中添加
您可以使用construct参数初始化对象，也可以稍后设置值
解决方案：
```python
类人员：
#定义类参数“name”
name=“个人”
def __init__（self，name=None）：
#self.name是实例参数
self.name=名称
jeffrey=个人（“jeffrey”）
print（“%s name is%s”%（Person.name，jeffrey.name））
nico=人物（）
nico.name=“nico”
print（“%s name is%s”%（Person.name，nico.name））
```

### Question 26:

Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

Solution

```python
def SumFunction(number1, number2):
	return number1+number2

print(SumFunction(1,2))
```
###问题26：
定义一个可以计算两个数字之和的函数。
提示：
定义一个以两个数字作为参数的函数。您可以在函数中计算和并返回值。
解决方案
```python
def SumFunction（数字1，数字2）：
返回编号1+编号2
打印（SumFunction（1,2））
```




### Question 27

Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.

Solution

```python
def printValue(n):
    print(str(n))

printValue(3)
```


###问题27
定义一个函数，该函数可以将整数转换为字符串并在控制台中打印。
提示：
使用str（）将数字转换为字符串。
解决方案
```python
def printValue（n）：
print（str（n））
打印值（3）
```



### Question 28

Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.

Solution

```python
def printValue(n):
    print(str(n))

printValue(3)
```

###问题28
定义一个函数，该函数可以将整数转换为字符串并在控制台中打印。
提示：
使用str（）将数字转换为字符串。
解决方案
```python
def printValue（n）：
print（str（n））
打印值（3）
```




### Question 29

Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.

Solution

```python
def printValue(s1,s2):
    print(int(s1)+int(s2))

printValue("3","4")
```

###问题29
定义一个函数，该函数可以接收字符串形式的两个整数，计算它们的和，然后在控制台中打印。
提示：
使用int（）将字符串转换为整数。
解决方案
```python
def printValue（s1，s2）：
print（int（s1）+int（s2））
printValue（“3”、“4”）
```
### Question 30

Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings

Solution




###问题30
定义一个可以接受两个字符串作为输入的函数，将它们连接起来，然后在控制台中打印。
提示：
使用+连接字符串
解决方案
"""

"""
Please write a program to print the running time of execution of "1+1" for 100 times.

计算执行“1+1”操作 100 次的运行时间。
"""


def times():
    print(timeit.Timer('for i in range(100):1+1').timeit())


"""
Please write a program to shuffle and print the list [3,6,7,8].

打乱list
"""


def shuffle_list():
    l = [3, 6, 7, 8]
    shuffle(l)
    print(l)


"""
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"]
 and the object is in ["Hockey","Football"].

编写一个程序，生成所有主语为 ["I", "You"]，动词为 ["Play", "Love"]，宾语为 ["Hockey", "Football"] 的句子。
提示：使用列表索引来获取列表中的元素。
"""


def concatenation_statement():
    for i in ["I", "You"]:
        for j in ["Play", "Love"]:
            for k in ["Hockey", "Football"]:
                print(i, j, k)


"""
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.

去掉所有偶数
"""


def del_even_nums():
    print([x for x in [5, 6, 77, 45, 22, 12, 24] if x % 2 != 0])


"""
By using list comprehension, please write a program to print the list after removing 
delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.


定义一个函数，输入一个列表，返回一个新的列表，其中删除掉所有能被 5 和 7 整除的元素。
使用输入列表调用函数，打印输出列表。  
"""


def comprehension_remove():
    l = [12, 24, 35, 70, 88, 120, 155]
    print([x for x in l if x % 5 != 0 and x % 7 != 0])


"""
By using list comprehension, please write a program to print the list after removing
 the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

去除偶数位元素
"""


def remove_even_number():
    print([x for (i, x) in enumerate([12, 24, 35, 70, 88, 120, 155]) if i not in (0, 2, 4, 6)])


"""
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array. 

生成一个3*5*8的3维列表
"""


def generate_3d_array():
    print([[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)])


"""

By using list comprehension, please write a program to print the list after removing 
the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

首先删除列表中的 0 号元素，然后删除 4 号元素，最后删除 5 号元素。  
打印删除后的列表

"""


def remove_element():
    l = [12, 24, 35, 70, 88, 120, 155]
    print(list(enumerate(l)))
    print([(i, x) for (i, x) in enumerate(l) if i not in (0, 4, 5)])


"""
By using list comprehension, please write a program to print the list after 
removing the value 24 in [12,24,35,24,88,120,155].

从list删除24
"""


def remove_num():
    l = [12, 24, 35, 24, 88, 120, 155]
    # print(l.remove(24))
    print(l)


"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

去重并保留原始顺序
"""


def sort_set_list(l: list):
    res = []
    sets = set()
    for i in l:
        if i not in sets:
            res.append(i)
            sets.add(i)
    print(res)
    return res


"""
Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

定义 Person 类和其两个子类 Male 和 Female 。
所有类都有一个名为"getGender"的方法，它可以打印出"Male"（对于 Male 类）和"Female"（对于 Female 类）
"""
"""
Please write a program which count and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:  abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1

计算并打印出控制台输入的字符串中每个字符的数量。
例如：如果将以下字符串作为输入传递给程序：abcdefgabc
那么，程序的输出应该是：
a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""


class Person(object):
    def __init__(self):
        pass

    def get_gender(self):
        pass


class Male(Person):
    def __init__(self):
        super().__init__()

    def get_gender(self):
        print('Male')
        return 'Male'


class Female(Person):
    def __init__(self):
        super().__init__()

    def get_gender(self):
        print('Female')
        return 'Female'


def get_str_counts(s: str):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1

    print('\n'.join(['%s,%s' % (k, v) for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)]))


"""
Please write a program which accepts a string from console and print it in reverse order.
Example:
If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:
ris etov ot esir
"""


def reverse_str(s: str):
    print(s[::-1])


"""
Please write a program which accepts a string from console and print the characters that have even indexes.
Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld

打印出具有偶数索引的字符
"""


def get_even_index(st: str):
    print(st[::2])


"""
【Please write a program which prints all permutations of [1,2,3]

Use itertools.permutations() to get permutations of list.

编写一个程序，输出列表 [1,2,3] 的所有排列。
提示：使用 itertools.permutations() 获取列表的排列。
"""


def permutations_list(l: list):
    print(list(permutations(l)))


"""
编写一个程序来解决中国古代的一个经典谜题：鸡兔同笼
农场里的鸡和兔子的35个头和94条腿。有多少只兔子和多少只鸡？
"""


def chick_rabbit(heads, legs):
    for chick in range(heads + 1):
        rabbits = heads - chick
        if chick * 2 + rabbits * 4 == legs:
            print(chick, rabbits)
    print(None)


if __name__ == '__main__':
    # print((218975.78 / 12) * 7 + 51880.46 + (16000 / 21.75 / 8) * 84 + ((16000 / 21.75) * 6))
    # get_nums()
    # print(fact(8))
    # make_dict(8)
    # handle_type('34,67,55,33,12,98')
    # test_string()
    # calculate_q('100,150,180')
    # li(4, 6)
    # sort_input('without,hello,bag,world')
    # str_upper()
    # sort_diff('hello world and practice makes perfect and hello world again')
    # num_divisible('0100,0011,1010,1001')
    # get_even_nums()
    # get_totals('hello world! 123')
    # get_upper_lower_nums('Hello world! 123')
    # sum_nums(9)
    # get_odd('1,2,3,4,5,6,7,8,9')
    # get_money()
    # check_pwd('ABd1234@1,a F1#,2w3E*,2We3345')
    # sort_tuple()
    # for i in DivisibleBySeven(30):
    #     print(i)
    # get_move_sqrt()
    # get_key_count('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')
    # chick_rabbit(35, 94)
    # permutations_list([1, 2, 3])
    # get_even_index('H1e2l3akjdhlauda 7q91288-09qwidphal4o5w6o7r8l9d')
    # reverse_str('H1e2l3akjdhlauda 7q91288-09qwidphal4o5w6o7r8l9d')
    # get_str_counts('qwertyuioqwertyuiasdfghjklertyuxcvbnmfghwerty')
    # male = Male()
    # female = Female()
    # male.get_gender()
    # female.get_gender()
    # sort_set_list([12, 24, 35, 24, 88, 120, 155, 88, 120, 155])
    # remove_num()
    # remove_element()

    # generate_3d_array()
    # remove_even_number()
    # comprehension_remove()
    # del_even_nums()
    # concatenation_statement()
    # shuffle_list()
    times()