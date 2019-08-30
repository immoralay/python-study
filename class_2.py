#1 现在有字符串：'hello python18 !'（注意点:转换之后单词之间有空格），转化成列表 li = [‘hello’,‘python18’,‘!’]
# a = 'hello python18 !'
# li = a.split()
# print(li)

#2.把 username = 'There is sweet man named yuze, 18 sui' 中的 'man' 字符串取出来
# username = 'There is sweet man named yuze, 18 sui'
# print(username[15 : 19])

#3.best_language = "     PHP is the best programming language in the world!      "。左右各有一个空格。
# 将给定字符串前后的空格除去，把PHP替换为Python，
# best_language = "     PHP is the best programming language in the world!      "
# b = best_language.strip()
# c = b.replace("PHP","Python")
# print(c)

#第二种方法
# import re
#
# best_language = "     PHP is the best programming language in the world!      "
# a = re.compile("PHP")
# b = a.sub("Python",best_language)
# c = b.strip()
# print(c)



# 4.演练字符串操作
# my_hobby = "Never stop learning!"
# 截取从 位置2 ~ 位置6 的字符串
# 截取从 位置2 ~ 末尾 的字符串
# 截取从 开始位置~ 位置6 的字符串
# 截取完整的字符串
# 从 索引3 开始，每2个字符中取一个字符
# 从右边开始截取，倒数第 2位置 到 倒数 5位置，步长为2
# 截取字符串末尾两个字符
# 字符串的逆序
# 说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），“索引”指的是字符的索引值（比如索引0，
# 代表的是第一个字符“N”）

# my_hobby = "Never stop learning!"
# print(my_hobby[1:6]) # 截取从 位置2 ~ 位置6 的字符串
# print(my_hobby[1:]) # 截取从 位置2 ~ 末尾 的字符串
# print(my_hobby[:5]) # 截取从 开始位置~ 位置6 的字符串
# print(my_hobby[:]) # 截取完整的字符串
# print(my_hobby[3::2]) # 从 索引3 开始，每2个字符中取一个字符
# print(my_hobby[-2:-6:-2]) # 从右边开始截取，倒数第 2位置 到 倒数 5位置，步长为2
# print(my_hobby[-2:]) # 截取字符串末尾两个字符
# print(my_hobby[::-1]) # 字符串的逆序
