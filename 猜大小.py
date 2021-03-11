import random
gnum = random.randint(1,100)
count = 0
while count < 8:
    num = int(input('请输入数字：'))
    count += 1
    if num == gnum:
        print(f'恭喜你猜中了，数字是{gnum}，猜测了{count}次')
        break
    elif num > gnum:
        print('猜测的数字太大了，继续加油！')
        continue
    else:
        print('猜测的数字有点小，再来一次')
else:
    print('太弱了，猜了5次还没猜出来，不和你玩了！')

