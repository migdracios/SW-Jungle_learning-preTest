# # # # # # # # # print('Hello, Jungle')

# # # # # # # # # a=3
# # # # # # # # # print(a)
# # # # # # # # # b=a
# # # # # # # # # print(b)
# # # # # # # # # a=5
# # # # # # # # # print(a,b)

# # # # # # # # # a=3
# # # # # # # # # a

# # # # # # # # # a = 4.8

# # # # # # # # # a = 7
# # # # # # # # # b = 2

# # # # # # # # # a+b     # 9
# # # # # # # # # a-b     # 5
# # # # # # # # # a*b     # 14
# # # # # # # # # a/b     # 3.5
# # # # # # # # # a//b    # 3 (몫)
# # # # # # # # # a%b     # 1 (나머지)
# # # # # # # # # a**b    # 49 (거듭제곱)

# # # # # # # # # a+3*b   # 13 (사칙연산 순서대로)

# # # # # # # # # a = 5
# # # # # # # # # a = a + 3   # 5에 3을 더한 값이 a에 저장
# # # # # # # # # print(a)
# # # # # # # # # a+=1
# # # # # # # # # print(a)



# # # # # # # # word1 = "jungle"
# # # # # # # # word2 = 'coding'

# # # # # # # # mac = "McDoanld's"
# # # # # # # # sentence = "He said, 'Hello!'"

# # # # # # # # a = 1
# # # # # # # # b = "a"
# # # # # # # # c = a
# # # # # # # # print(a,b,c)

# # # # # # # # # d = x

# # # # # # # # # d = "x"

# # # # # # # # a = "3"
# # # # # # # # b = "5"
# # # # # # # # print(a+b)

# # # # # # # # myname = 'jungle'
# # # # # # # # print(myname.upper())

# # # # # # # myemail = "test@gmail.com"
# # # # # # # result = myemail.split('@')

# # # # # # # print(result[0])
# # # # # # # print(result[1])

# # # # # # # result2 = result[1].split('.')

# # # # # # # print(result2[0])
# # # # # # # print(result2[1])

# # # # # # txt = '서울시-마포구-망원동'
# # # # # # result = txt.replace('-','>')
# # # # # # print(result)

# # # # # x = True
# # # # # y = False

# # # # # print(4>2)
# # # # # print(5<1)
# # # # # print(6>=5)
# # # # # print(4<=4)
# # # # # print(3==5)
# # # # # print(4!=7)

# # # # a = 4>2
# # # # print(not a)

# # # # b=2!=2

# # # # print(a and b)
# # # # print(a or b)

# # # def f(x):
# # #     return 2*x+3

# # # print(f(2))

# # # def sum_all(a,b,c):
# # #     return a+b+c
# # # print(sum_all(1,2,3))

# # def oddeven(num):
# #     if num % 2 == 0:
# #         return True
# #     else:
# #         return False

# # result = oddeven(20)
# # print(result)

# def is_adult(age):
#     if age >20:
#         print('iAmAnAdult')
#     elif age >=13:
#         print('iAmaTeenager')
#     else:
#         print('iAmaChild')

# print(is_adult(23))

fruits = ['사과', '배', '감', '귤']

for fruit in fruits:
    print(fruit)