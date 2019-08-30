#.删除如下列表中的"矮穷丑"，写出能想到的所有方法
#info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
#方法一（根据值删除元素）
info.remove("矮穷丑")
print(info)
#方法二(按照索引位删除元素)
info.pop(3)
print(info)
#方法三（del语句删除索引位置的元素）
del info[3:4]
print(info)

# 有5道小题：
# a. 某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
# c, 平台为了保护你的隐私，需要你删除你的联系方式；
# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
# e, 你进一步添加自己的兴趣，至少需要 3 项。一经确定，不可单独修改各个兴趣点。
#a:解答 某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
name = input("请输入您的姓名: " )
gender = input("请输入您的性别: ")
age = input("请输入您的年龄: ")
data = {"name":name,"gender":gender,"age":age}
#b:解答 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
high = input("请输入您的身高: ")
tel = input("请输入您的联系方式：")
data.update({"high":high,"tel":tel})
#c:解答
data.pop("tel")
#d:解答
nickname = input("请输入您的花名: ")
high_new = input("请输入你要修改的身高: ")
data["high"]=high_new
data["nickname"]=nickname
think = input("请问是否要修改信息？是：Y 否：N")
if think == "Y":
  while True:
     choice = input("请输入你想要修改的其他信息: nickname, name, gender, age:")
     if choice in data.keys():
        newValue = input("请输入你想要修改的" + choice + "值:")
        data[choice] = newValue
        print("您已修改完毕")
     else:
        print("未找到该信息")
     check = input("是否输入结束修改？是：Y 否：N")
     if check == 'Y':
        print("您已结束修改")
        break
else:
    print("您本次不做修改")


#f:解答
while True:
  like_one = input("请输入您的兴趣，并以空格断开: ")
  like_list = list(like_one.split())
  data["兴趣"] = like_list
  if len(like_list) >= 3:
      break
  print("请输入至少3项爱好")
print(data)






# 3、现在有一个列表 li2=[1，2，3，4，5]，
# 第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
# 第二步：对li2进行排序处理
# 第三步：请写出删除列表中元素的方法，并说明每个方法的作用
# #第一步
li2=[1,2,3,4,5]
li3=[11,22,33]
li2.extend(li3)
li2.insert(0,0)
li2.insert(4,66)
print(li2)
# #第二步
# #逆转排序
li2.sort(reverse=True)
print(li2)
# # #反转排序
li2.reverse()
print(li2)
# # #冒泡排序
for i in range(len(li2)-1):
    for l in range(len(li2)-1-i):
        if li2[l]<li2[l+1]:
           li2[l],li2[l+1] = li2[l+1],li2[l]
else:
    print(li2)
# #第三步：请写出删除列表中元素的方法，并说明每个方法的作用
# #方法一（根据值删除元素）
li2.remove(0)
print(li2)
# #方法二(按照索引位删除元素)
li2.pop(3)
print(li2)
# #方法三（del语句删除索引位置的元素）
del li2[3:4]
print(li2)



