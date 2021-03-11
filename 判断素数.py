# # 素数，一个数字如果说只能被1和本身整除，这个数字就是素数
# # 如何判断一个数字是不是素数呢？ 让这个数字从2 开始整除，到数字键1 结束，如果都不能被整除，就是素数
#
# # num = int(input('请输入用来判断的数字：'))
# num = 1
# while num <= 200:
#     i = 2
#     while i < num:
#         if num % i == 0:
#             # 如果出现一个数字，能整除，则说不他不是素数
#             # print(f'{num}不是素数')
#             break
#         # else:
#         i += 1
#             # continue
#     else:
#         print(num, end=' ')
#     num += 1

input_str = input('请输入一个字符串：')
for i in input_str:
    if i == 'q':
        break
    elif i == ' ':
        continue
    print(i , end='')
