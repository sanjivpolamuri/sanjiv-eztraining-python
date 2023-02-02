# temp > 45 ==> hottest
# 40 < temp <= 45 ==> hot
# 25 < temp <= 40 ==> moderate
# 10 < temp <= 25 ==> cold
# temp <= 10 ==> chill
# l = [1, 2.3, 4, 'sum', 5]
# print(l)
# print(l[2])
# print(type(l))
# print(l[0:3])
# print(l[:3])
# print(l[:])
# print(l[2:])
# print(l[-2])
# print(l[::-1])
# print(l[::-2])
# print(l[::2])
# print(l[:-1])
# print(l[-4:])
'''
list operations:
append()
extend()
insert()
remove()
pop()
clear()
index()
sort()
count()
reverse()
copy()
'''
# l.append(4)
# print(l)
# l.extend(['hi', 'hello'])
# print(l)
# l.insert(2, 'hoo')
# print(l)
# l.remove(4)
# print(l)
# l.pop()
# print(l)
# print(l.index('hoo'))
# a = ['u', 'gh', 'shjg', 'shr', 'g', 'a']
# a.sort()
# print(a)
# print(l.count('hoo'))
# l.reverse()
# print(l)
# b = l.copy()
# print(b)
# l.clear()
# print(l)
'''
# create a list with 10 items print the elements one by one.
l = [1, 2, 3, 4, 5, 'hi', 'hello', 4, 5, 6]
for i in range(len(l)):
    print(l[i])
# for j in l:
#     print(j)
# create a list with 5 float nums, find and display sum and avg of the list.
f = list(map(float, input('Enter 5 float type numbers: ').split( )))
sum = 0
avg = 0
for k in f:
    sum += k
print('Sum: ', sum)
print('Average: ', sum / len(f))
# after creating a list with 6 elements from the user extract only even numbers and print.
p = list(map(int, input('Enter 6 numbers: ').split( )))
print('Prime numbers: ')
for j in p:
    if j % 2 == 0:
        print(j)
        '''
# _________________________neon numbers________________________
# a = int(input('Enter a number: '))

# n = a*a
# sum = 0
# n = str(n)
# lenOfN = len(n)
# for i in range(lenOfN):
#     sum += int(n[i])
# if sum == a:
#     print('Entered number is a neon number')
# else:
#     print('Entered number is not a neon number')


# l = list(map(int, input('Enter a list of numbers: ').split( )))
# for i in range(len(l)):
#     sum = 0
#     n = l[i]*l[i]
#     n = str(n)
#     lenOfN = len(n)
#     for j in range(lenOfN):
#         sum += int(n[j])
#     if sum == l[i]:
#         print(l[i], 'is a neon number')
#     else:
#         print(l[i], 'is not a neon number')
  
# l = list(map(int, input('Enter a list of numbers: ').split( )))
# prod = 1
# sum = 0
# for i in range(len(l)):
#     prod *= l[i]
#     sum += l[i]
# # print(prod)
# if prod < 750:
#     print('product: ', prod)
# else:
#     print('Sum: ', sum)
# ______________________ list comprehension_______________________
# numbers = [elements for elements in 'Great Afternoon']
# print(numbers)
# l = ['delhi', 'vizag', 'vijayanagaram', 'kolkata', 'bhimavaram']
# city = []
# for n in l:
#     if 'v' in n:
#         city.append(n)
# print(city)
# l1 = [2**x for x in range(2, 10)]
# print(l1)
# l2 = [a for a in range(100, 201, 20)]
# print(l2)
# l3 = [1, 2, 3, 4, 5]
# l4 = [i for i in l3 if i < 4]
# print(l4)
# _________________________SETS__________________________
# s = {1, 3, 4, 2, 1, 1, 3, 7, 'hi'}
# s.add(21)
# print(s)
# s.update([20, 40, 'hi'])
# print(s)
# s.discard(20)
# print(s)
# s.remove(40)
# print(s)
# s1 = {1, 2, 3}
# s2 = {4, 5, 6, 1, 2}
# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s2 - s1)
# _____________________superset__________________________
# s = {1, 2, 3}
# s1 = {1, 2, 3, 4, 5}
# print(s1.issuperset(s))
# _____________________symettric difference________________________
# s = {1, 2, 3}
# s1 = {1, 2, 3, 4, 5}
# print(s1^s)
# print(s.symmetric_difference(s1))
# _____________________Tuples__________________________
# t = (1, 3, 4, 3, 6)
# print(type(t))
# print(t.count(4))
# print(t.count(4))
# print(t.index(4))
# _______________Dictionary__________________
'''Dictionary contains element with 2 units (keys and values)
Keys must be unique'''
# d = {1: 'one', 2: 'two'}
# print(type(d))
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# d = {'syl': 'techno', 'chaaru': 'meizu'}
# print(type(d))
# print(d['syl'])
# print(d.get('syl'))
l = ['hi', 'hello']
d = dict.fromkeys(l ,50)
print(d)
d1 = {}.fromkeys(l, 100)
print(d1)
d.update({'c': 89, 'd': 32})
print(d)
d.pop('c')
print(d)
d.popitem()
print(d)









