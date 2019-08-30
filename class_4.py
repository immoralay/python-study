#1.请写出if判断语句的格式（考虑 2 种典型的 if...if 场景。）
#常见的第一种
# if 要判断的条件:
#     条件成立时，要做的事情
#     ……
# else:
#     条件不成立时，要做的事情
#常见的第二种
# if 条件1:
#     条件1满足执行的代码
#     ……
# elif 条件2:
#     条件2满足时，执行的代码
#     ……
# elif 条件3:
#     条件3满足时，执行的代码
#     ……
# else:
#     以上条件都不满足时，执行的代码
#     ……
#常见的第三种
# if 条件 1:
#     条件 1 满足执行的代码
#     ……
#     
#     if 条件 1 基础上的条件 2:
#         条件 2 满足时，执行的代码
#         ……    
#         
#     # 条件 2 不满足的处理
#     else:
#         条件 2 不满足时，执行的代码
#
# # 条件 1 不满足的处理
# else:
#     条件1 不满足时，执行的代码

#2、判断是否为闰年
# 输入一个有效的年份（如：2019），判断是否为闰年
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
a = int(input("请输入年份："))
if a % 4 ==0 and a % 100 !=0:
    print("该年份为普通闰年")
elif a % 400 == 0:
    print("该年份为世纪闰年")
else:
    print("该年份不是闰年")

#3、使用条件语句完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
#电脑随机出拳比较胜负，显示用户胜、负还是平局。
#-----石头剪刀布游戏开始----
#请按下面提示出拳
#【1】石头【2】剪刀【3】布【4】退出
#请输入你的选项 1
#你的出拳为：石头 电脑出拳为：剪刀 你胜利了
#【1】石头【2】剪刀【3】布【4】退出
#请输入你的选项4
#游戏结束

#电脑随机出拳
# 使用随机数，首先需要导入随机数的模块 —— “工具包”
# import random
# 导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
# random.randint(a, b)，返回[a, b]之间的整数，包含a和b
# random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10
# random.randint(4, 4)  # 结果永远是 4
# random.randint(25, 12)  # 该语句是错误的，下限必须小于上限

#该题进行了一个统计次数的拓展课忽略

import random
#角色代表
role = {1:"石头",2:"剪刀",3:"布",4:"退出"}
count_human = 0
count_pc = 0
count_peace = 0
while True:
#人类出拳
    human = int(input("请按照下面提示出拳：\n1 石头 2 剪刀 3 布 4 退出 \n请输入你的选项："))
#电脑出拳
    pc = (random.randint(1,3))
#输赢判断
    win_number = human - pc
    if human == 4:
        print("游戏结束")
        break
    elif win_number==-2 or win_number==1:
        count_pc += 1
        print("您的出拳为{}，电脑出拳{},电脑胜利".format(role[human],role[pc]))
    elif win_number==-1 or win_number==2:
        count_human += 1
        print("您的出拳为{}，电脑出拳{},人类胜利".format(role[human],role[pc]))
    elif win_number==0:
        count_peace += 1
        print("您的出拳为{}，电脑出拳{},平局".format(role[human],role[pc]))
    else:
        print("信息无效")
print("人类赢了{}次,电脑赢了{},平局{}次".format(count_human, count_pc, count_peace))




#4、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
#如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或
#20%）和最终价格。

price = float(input("您的购买金额："))
if 50 <= price <= 100:
   total = price - price * 0.1
   print("您享受10%的折扣优惠，最终价格为：{} ".format("%.2f" % total))
elif price > 100:
   total = price - price * 0.2
   print("您享受20%的折扣优惠，最终价格为：{}".format("%.2f" % total))
elif  0< price < 50:
   print("您本次消费不享受优惠，最终价格为：{}".format("%.2f" % price))
else:
   print("您的价格输入错误")

# wrong_number = 0
# while wrong_number<3 :
#     price = float(input("您的购买金额："))
#     if 50 <= price <= 100:
#        total = price - price * 0.1
#        print("您享受10%的折扣优惠，最终价格为：{} ".format("%.2f" % total))
#        break
#     elif price > 100:
#        total = price - price * 0.2
#        print("您享受20%的折扣优惠，最终价格为：{}".format("%.2f" % total))
#        break
#     elif  0< price < 50:
#        print("您本次消费不享受优惠，最终价格为：{}".format("%.2f" % price))
#        break
#     else:
#        print("您的价格输入错误，请重试")
#        wrong_number += 1
#        if wrong_number == 3:
#           print("您错误次数已经达到3次，感谢您的使用")










