# i = 1
#
# while i < 100:
#     if (i % 7 == 0) or (i % 10 == 7) or (i // 10 == 7):
#         print('过。。。')
#     else:
#         print(i)
#     i += 1

for i in range(1,100):
    if (i % 7 == 0) or (i % 10 == 7) or (i // 10 == 7):
        print('过。。。')
    else:
        print(i)