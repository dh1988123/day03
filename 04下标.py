# 下标也称为索引，是一个整型的数字，可以是正数，也可以是负数
# 正数下标是从 0 开始的，表示第一个字符， -1 表示最后一个字符

my_str = 'hello'
# 下标的使用语法  变量[下标]

print(my_str[0])
print(my_str[1])
print(my_str[-1])
print(my_str[-3])

# len() 函数可以得到字符串的长度
print(len(my_str))
# 使用正数下标书写字符串中最后一个元素
print(my_str[len(my_str) - 1])