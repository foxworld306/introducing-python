# m开头的单词首字母大写
# song = """When an eel grabs your arm,
#     And it causes great harm,
#     That's - a moray!"""

# print(song.replace('moray', 'Moray'))


#使用旧格式化，分别使用'roast beef', 'ham', 'head'和'clam'插值
# question = (
#     "my kitty cat likes %s," % "roast beef", 
#     "my kitty cate likes %s," % "ham", 
#     "my kitty cat fell on his %s" % "head",
#     "And now thinks he's a %s." % "clam"
# )

# print(question)

# num = 1
# while num <= 5:
#     print(num)
#     num += 1
#     print(num)

# 输入的首字母大写，按q退出
# while True:
#     stuff = input("string to capitalize [type q to quit]:")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

# 读入一个整数，如果是奇数，则计算平方；偶数则跳过。按q退出
# while True:
#     num = input("input a number [type q to quit]:")
#     if num == "q":
#         break
#     number = int(num)
#     if number % 2 == 0: #偶数
#         continue
#     print(number, "squared is:", number*number)

# 查找偶数，有偶数则跳出循环，否则报错
# numbers = [1,3,5, 6]
# position = 0
# while position < len(numbers):
#     num = numbers[position]
#     if num % 2 == 0:
#         print('Found even number', num)
#         break
#     position += 1
# else:
#     print('No even number found')

# 6.2.3 查找字符串中某个字符并计数
# word = 'thus!'
# length = 0
# num = 0
# while length < len(word):
#     for letter in word:
#         print(letter)
#         length += 1
#         if letter == 'o':
#             num += 1
#     print('there are', num, 'O')

# range() & list
# for X in range(0, 10, -1):
#     print(X)
# x = list(range(0,3))
# print(x)

# 7.1.1 create a tuple
# empty_tuple = ()
# print(empty_tuple)
# one_ele = ('come',)
# print(one_ele)
# 6.5 01 print a list
# list = [3, 2, 1, 0, -1]
# print(*list, sep='\n')

# for a in list:
#     print(a)

# 6.5 02
# guess_me = 7
# number = 1
# while number < guess_me:
#     print('too low')
#     number+=1
#     if number == guess_me:
#         print(number)
#         print('found it')
#         break
#     if number > guess_me:
#         print('oops')
#         break
  
# 6.5 03
# guess_me = 5
# list = range(10)
# for a in list:
#     if a < guess_me:
#         print('too low')
#     if a == guess_me:
#         print(a)
#         print('found it')
#         break

#7.1.1 tuple
# new_tuple = ('hear', 'lesson', 'come')
# print(new_tuple)
# a, b, c = new_tuple
# print(a)
# print(b)
# print(c)

#switch tuple

# a = 'sdfjdfs'
# b = 'adfasfe'
# a, b = b, a
# print(a)
# print(b)

# create a tuple from a list
# list = ['a', 'b', 'c', 'd']
# print(tuple(list))

# copy tuple
# list = ('yada',) * 3
# print(list)

#compare tuple
# a = (7, 2)
# b = (7, 2, 9)
# print( a==b)
# print(a <= b)

# for and in with tuple
# list = ('come', 'on', 'baby')
# for word in list:
#     print(word)

# tuple cannot be changed. it can be plused to a new tuple
# a = ('come', 'on')
# b = ('baby',)
# print(a+b)

# empty list
# emptylist = [ ]
# print(emptylist)
# another_emptylist = list()
# print(another_emptylist)

# transfer other data types to a list
# list = list('cats')
# print(list)
# a_tuple = ('come', 'on')
# list = list(a_tuple)
# print(list)
# a_string = '06/29/2022'
# list = list(a_string.split('/'))
# print(list)
# a_string = '0/6//2/9//2022'
# list = list(a_string.split('//'))
# print(list)

# list = ['come', 'on', 'baby']
# # print(list[0]+list[2])
# # print(list[0:2])
# # print(list[::-1])
# list.reverse()
# print(list)

# Add a new element to a list
# a = ['come', 'on']
# a.append('baby')
# print(a)

# Insert an element to a list
a = ['come', 'on', 'baby']
# a.insert(1, 'baby')
# print(a) 
# a.remove('on')
# print(a)
# a.pop(1)
# print(a)
# a.clear()
# print(a)

# print(a.index('on'))
# print('on' in a)
# print(a.count('on'))
# print('*'.join(a))
# b = '*'.join(a)
# c = b.split('*')
# print(c)
# print(sorted(a))
a.sort()
print(a)