#密碼重設程式
password = 'a123456' #定義在迴圈外面
x = 3 #定義在迴圈外面,剩餘機會
while x > 0:
    pwd = input('請輸入密碼：')
    if pwd == password:
        print('登入成功')
        break
    else:
        x = x - 1
        print('密碼錯誤！還有', x, '次機會')
        