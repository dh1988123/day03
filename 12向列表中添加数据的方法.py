# 向列表中添加数据的方法，都是直接在原列表中进行添加的，不会返回新列表
my_list = ['郭德纲', '于谦', '小岳岳', '孙越']
print(my_list)
# 列表.append(数据) 向列表的尾部追加数据
my_list.append('aa')
print(my_list)
rasult = my_list.append(12) # 不要这样书写
# print(rasult) # None 关键字，表示空

# 列表.insert(下标， 数据) 在指定下标位置进行添加数据
my_list.insert(0, 'isaac')
print(my_list)
# print(my_list.insert(5, 3.14)) 不能这样书写， None
my_list.insert(5, 3.14)
print(my_list)

# 列表.extend(可迭代对象) str 列表，会将可迭代对象中的数据逐个添加到原列表的末尾
my_list.extend('hel')
print(my_list)
my_list.extend([1, 'python', 3])
print(my_list)