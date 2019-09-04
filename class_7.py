#1. 将用户输入的所有数字相乘之后对20取余数
#用户输入的数字个数不确定
def number(*args):
    count = 1
    for i in args:
        count *= i
        new_count = count % 20
    return(new_count)
print(number(1,101,4,5,6,7))

#请忽略以下做法
# import sys
#
# def main(argv):
#  for arg in argv[1:]:
#   print(arg)
#
# if __name__ == '__main__':
#  main(sys.argv)



#2，编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def changdu(list):
    if len(list)>2:
        list_new = list[:2]
    return list_new

list= changdu([1,2,3,4,5,6])
print(list)



# 3， 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
def real_number(dict_number,str_number):
    if  not str_number in dict_number.keys():#如果这里是values的话，那么我后续的同样的值都会作为相同的key存在字典里，这样没有任何意义
        dict_number[str_number]=''
        return(dict_number)
dict_number = {'we':'','wr':'','wq':'','wv':''}
str_number = 'wt'
print(real_number(dict_number,str_number))





#4， 通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
def calculator(x,y):
    number = input('提示选择【1】加 【2】减【3】乘 【4】除，请输入：')
    if number == '1':
        return(x+y)
    elif number == '2':
        return(x-y)
    elif number == '3':
        return(x*y)
    elif number == '4':
        return(x//y)
    return ('输入错误')
print(calculator(6,3))


#5 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，然后显示一条消息
# 指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
#函数体做法
def count():
    sum = 0
    sum_new = 0
    while sum <10:
        age = int(input('请输入你的年龄：'))
        gender = input('请输入你的性别：')
        if 15<=age<=22:
            if gender == '女孩':
                sum_new += 1
                print('可以加入足球队')
            elif gender == '男孩':
                print('由于您是男孩，所以不能加入足球队')
            else:
                print('输入错误，请重试')
        else:
            print('年龄不符，所以不能假如足球队')
        sum += 1
    return('本次满足条件的拉拉队员共{}人'.format(sum_new))
print(count())

#whlie 循环做法
sum = 0
sum_new = 0
while sum <10:
    age = int(input('请输入你的年龄：'))
    gender = input('请输入你的性别：')
    if 15<=age<=22:
        if gender == '女孩':
            sum_new += 1
            print('可以加入足球队')
        elif gender == '男孩':
            print('由于您是男孩，所以不能加入足球')
        print('输入错误请重试')
    print('年龄不符，所以不能假如足球队')
    sum += 1
print('本次满足条件的拉拉队员共{}人'.format(sum_new))

#今日做作业总结（老师不用看，自己的随笔）：
#1、根据具体的场景决定的。 如果if之后还会继续执行之后的代码 那么else就不能省略 因为else里的逻辑是if的分支逻辑，不能一下走两个分支
#如果if之后不会继续执行同生命周期的代码 那么可以省略
#2、函数的行参实参最好一致