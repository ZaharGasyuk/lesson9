# def g():
#     print(10+10)
# g()


# def g(a,b):
#     print(a+b)
# g(1000,1000)
    

# from math import sqrt
# def function(side1,side2):
#     result = sqrt((side1*side1)+(side2*side2))
#     print(result)
# function(5,10)

# import string
# name_surname = 'Zahar Gasyuk'
# values = 'aouei'
# b = string.ascii_lowercase

# def func(text):
#     a = 0
#     c = 0
#     for i in text:
#         if i in values:
#             a += 1
#     for z in text:
#         if z.lower() in b and z.lower() not in values:
#             c += 1
            
#     print(f'Кількість голосних: {a},а приголосних: {c}')
            

# func(name_surname)


for i in range(0,6):
    for z in range(0,i+1):
        print('*',end = '')
    print()
for i in reversed(range(0,6)):
    for z in range(0,i+1):
        print('*',end = '')
    print()

