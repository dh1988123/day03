# 切片可以获取一段数据，多个数据，下标（索引只能获得一个数据）
# 切片语法: 变量[start: end: step], 会得到一个新的字符串
# start 开始位置的下标
# end 结束位置的下标
# step 步长，下标之间的间隔，默认是1
my_str = 'hello'
my_str1 = my_str[2:4:1]
print(my_str1)
# step 如果是1 ，即默认值，可以不写
my_str2 = my_str[2:4]
print(my_str2)

# end 位置不写，表示是len() ，即可以取到最后一个元素
my_str3 = my_str[2:]
print(my_str3)
# start 位置也可以省略不写，表示0
my_str4 = my_str[:3]
print(my_str4)

# start 和 end 都不写，但是冒号需要写
my_str5 = my_str[:]
print(my_str5)

print(my_str[-4: -1])
print(my_str[::-1])
print(my_str[::2])