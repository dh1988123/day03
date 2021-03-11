# my_str.join(可迭代对象)
# 可迭代对象，str, 列表(需要列表中的每一个数据都是字符串类型)
# 将my_str 这个字符串添加到可迭代对象的两个元素之间
# 返回值： 一个新的字符串, 不会改变原字符串的值

my_str = '_'.join('hello')  # 会把_加入到hello每两个元素之间
my_str = '_*_'.join('hello')  # 会把_加入到hello每两个元素之间
print(my_str)

# 定义列表
my_list = ['hello', 'cpp', 'python']
print("_".join(my_list))    # hello_cpp_python







