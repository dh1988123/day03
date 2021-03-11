my_list = [1, 2, 3, 4, 5, 6, 9]
# 1. 根据元素的数据值删除 remove(数据值), 直接删除原列表中的数据
my_list.remove(4)
print(my_list)
# my_list.remove(4) 程序报错，要删除的数据不存在


# 2. 根据下标删除
# 2.1 pop(下标) 默认删除最后一个数据，返回删除的内容
num = my_list.pop() # 删除最后一个数据 9
print(num)
print(my_list) # [1, 2, 3, 5, 6]

num = my_list.pop(2) # 删除下标为2的数据即 5
print(num)
print(my_list) # [1, 2, 5, 6]
#my_list.pop(12) # 删除下标不存在，会报错

# 2.2 del 列表[下标]
del my_list[1]
print(my_list)

# del my_liest[10] 删除不存在的下标，会报错

