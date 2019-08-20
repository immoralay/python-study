#一、现在有字符串：str1 = 'python cainiao 666'
# 1、请找出第 5 个字符。
# 2、请复制一份字符串，保存为 str_two
 #3、请找出最中间的字符。

#1.1解答：
str1 = 'python cainiao 666'
print(str1[4])
#或者
print(str1[-14])

#1.2解答：
str1 = 'python cainiao 666'
str_two = a[:]
print(str_two)

#1.3解答：
str1 = '12345'
a = len(str1)
if a%2 == 0:
    print(str1[a//2-1:a//2+1])
else:
    print(str1[a // 2:a//2+1])
#解题思路：根据len是个int类型
#因为除法生成的新的数据类型肯定是浮点数 而数组取值不能是浮点数 必须是整数，所以除法要用"//"


#二、用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False
# （提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法转换为数值类型，再做判段，）
#解答：
a = int(input("请输入数字:"))
if a%2 == 0:
    print("True")
else:
   print("False")


#三、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！
prince = float(input("请输入橘子的价格: "))
weight = float(input("请输入橘子的重量: "))
total = prince * weight
print(round(total))


#四、a = True , b = (99 // 2 == 1), c = 0 判断真假：
#1， not b = True
#2， a and b = Flase
#3， a and b and c = Flase
#4， (a or c) and b = Flase

a = True
b = (99 // 2 == 1)
c = 0
print((a or c) and b)
print(not b)
print(a and b)
print(a and b and c)
#最后一道题是自己主管先判断，然后再走程序进行验证