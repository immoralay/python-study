#1.求三个整数中的最大值
#提示：三个整数使用input提示用户输入
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
c = int(input("请输入第三个数字："))
lie = [a,b,c]
for i in range(2):
    for j in range(i):
        if lie[j] > lie[j + 1]:
           lie[j], lie[j + 1] = lie[j + 1], lie[j]
print("最大数字为{}".format(lie[2]))


#2.分别使用for和while打印九九乘法表
# 提示：
# 输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
# 1 * 1 = 1
# 1 * 2 = 2    2 * 2 = 4
# 1 * 3 = 3    2 * 3 = 6      3 * 3 = 9
# 1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16
# 1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25
# 1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36
# 1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49
# 1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64
# 1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81

#for解题
#解题思路：i 为行数，j 为列
#i=1，j=1     i=1 j = range(1,1) 即range(1,i+1)
#i=2,j=1 2     i=1 j = range(1,2)
#i=3,j=1 2 3    i=1 j = range(1,3)
for i in range(1,10):#行数举例：                   1       2        3
    for j in range(1,i+1):# 对应行数下的乘法数：     1       1 2      1 2 3
        print("{}*{}={} ".format(j,i,j*i),end ='')#"end"代表不换行输出
    print()#print自带有换行输出的意义

#while解题
a = 1
while a<=9:
      j = 1
      while j < a + 1:
          print("{}*{}={} ".format(j,a,j*a),end ='')
          j = j + 1
      print()
      a=a+1


#3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# 当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in black_list[:]:
       black_list.remove(i)
       print(black_list)


a = len(black_list)
j = 0
while j < a:
      del black_list[0]
      print(black_list)
      j += 1





#4.使用循环实现排序算法
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
a=[1,7,4,89,34,2]
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j + 1]:
           a[j], a[j + 1] = a[j + 1], a[j]
print(a)


# 5、从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
# a.定义一个函数，接收用户输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best
#第一种方法
user = input("请输入用户名：")
pwd = input("请输入密码：")
def user_info(human,words):#函数定义 形参
    if human == "lemon" and words == 'best':
        print("登陆成功")
    else:
        print('用户名或密码错误')
    return
user_info(user,pwd)#函数调用 实参

#第二种
user = input("请输入用户名：")
pwd = input("请输入密码：")
def user_info(human,words):
    if human == "lemon" and words == 'best':
        return("登陆成功")
    else:
        return('用户名或密码错误')
print(user_info(user,pwd))#函数调用，实参




