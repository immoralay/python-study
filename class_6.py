# 1.编写如下程序
# 尝试函数部分分装：
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
count = {1:"周一",2:'周二',3:'周三',4:'周四',5:'周五',6:'周末',7:'周末'}
def week():
    while True:
        number = int(input("请输入1～7七个数字: "))
        if number in count:
            return count[number]
        elif number == 0:
            return "exit"
        else:
            print("输入有误，请重新输入！")
print(week())

# 2.列表去重
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
#利用for循环
# a = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# new_a = []
# for i in a:
#     if not i in new_a:
#         new_a.append(i)
# print(new_a)

#set 方法去重
# a = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# new_a = list(set(a))
# print(new_a)

#使用字典中fromkeys()的方法来去重
# a = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# new_a = list({}.fromkeys(a).keys())
# print(new_a)

#3.将两个变量的值进行交换（a = 100, b = 200）
# 交换之后，a = 200， b = 100， 使用函数。
# def exchange(x,y):
#     x,y = y,x
#     return(x,y)
# print(exchange(100,200))

#4.编写如下程序
# 尝试函数部分封装：
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
#低于18.5： 过轻   18.5-25：   正常    25-28：      过重   28-32：      肥胖   高于32：   严重肥胖
# high = float(input('请输入你的身高（m）：'))
# weight = float(input('请输入你的体重(公斤)：'))
# def BMI(tall,weight_new):
#     number = weight_new / (tall ** 2)
#     print("%.2f" % number)
#     if number < 18.5:
#         return("过轻")
#     elif 18.5<=number<=25:
#         return('正常')
#     elif 25<number<=28:
#         return ('过重')
#     elif 28<number<=32:
#         return('肥胖')
#     return('严重肥胖')
# print(BMI(high,weight))