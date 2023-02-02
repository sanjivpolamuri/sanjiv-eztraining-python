# Intro to python
# print(type(3+5j))
# print(id(32))
# print(isinstance(23, int))
# print(isinstance(23, bool))
# print(isinstance(True, bool))
# print(isinstance(0, bool))
# a = 12
# print(f"the value of a is: {a}")
# print('input')
# print('_____')
# num1 = int
# (input('Enter first integer: '))
# num2 = int(input('Enter second integer: '))
# num3 = int(input('Enter third integer: '))
# num4 = float(input('Enter first float: '))
# num5 = float(input('Enter second float: '))
# num6 = float(input('Enter third float: '))
# str1 = input('Enter first string: ')
# str2 = input('Enter second string: ')
# comp = complex(input('Enter complex number: '))
# print('output')
# print('_____')
# print('First integer: ', num1)
# print('Second integer: ', num2)
# print('Third integer: ', num3)
# print('First float: ', num4)
# print('Second float: ', num5)
# print('Third float: ', num6)
# print('First string: ', str1)
# print('Second string: ', str2)
# print('Complex number: ', comp)
# print('2nd _____')
# kumarBought = 75
# sam = kumarBought/ 2
# kumarGot = sam/ 2
# print('Kumar is having: ', kumarGot, 'kgs')
# print('Sam is having: ', sam, 'kgs')
# print('3rd _____')
# print('final result: ', (3*36.32 + 56.19) - 10)
# print('4th _____')
# positiveNum = int(input('Enter a positive number: '))
# negativeFloat = float(input('Enter a negative float: '))
# print('result: ', positiveNum*negativeFloat)
# print(3 <3)
# print(3 <=3)
# print(3 >3)
# print(3 >=3)
# print(3 ==3)
# print(3 !=3)
# print(10<12 and 10 < 1)
# print(10 > 1 and 10 < 9)
# print(10 < 12 or 10 < 1)
# print(10 > 1 or 10 < 9)
#__________
#Multiple inputs within single line
# n1, n2 = int(input('Enter: ')), int(input('Enter: '))
# print(n1, n2)
# sum = n1 + n2
# print(sum)
# n3, n4 = input('Enter: ').split(',')
# print(n3,n4)
# n5, n6 = input('Enter: ').split( )
# print(n5,n6)
# x = input("Enter: ").split( )
# print(x)
# print(type(x))
# print(type(x[1]))
# print(type(x[0]))

# _______Programs____________
# 1st_______________
n1, n2 = input('Enter: ').split( )
n1, n2 = int(n1), int(n2)
temp = n1
n1 = n2
n2 = temp
print('n1 and n2 values are: ', n1, n2)
# 2nd___________________
a, b = input('Enter: ').split( )
a, b = int(a), int(b)
a = a + b
b = a - b
a = a - b
print(a, b)
# 3rd_________________
length, breadth = input('Enter length and breadth: ').split( )
length, breadth = int(length), int(breadth)
area = length*breadth
perimeter = 2*(length+breadth)
print('area of the rectangle is: ', area)
print('perimeter of the rectangle is: ', perimeter)

