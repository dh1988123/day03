
while True:
    user = input('请输入用户名：')
    pwd = input('请输入密码：')

    if user == 'python' and pwd == '123456':
        print('欢迎光临！')
        break
    else:
        print('输入错误，请重新输入！')