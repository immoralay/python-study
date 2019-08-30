
import random

lie = []
#徐大爷想要生成随机整数列表
for q in range(100):#100个参数的列表
    lie.append(random.randint(1, 1000))#列表取值是1到1000，random是python里随之取值的函数，randint是取整
print("徐爷要的表", lie)
#徐大爷要的排序
l = len(lie)
for i in range(l-1):#外层循环
 for n in range(l-1-i):#内层循环
   if lie[n]>lie[n+1]:
    lie[n],lie[n+1] = lie[n+1],lie[n]
else:
    print(lie)


