
#题目：统计出文章中出现频率最高的五个单词，输出相应频次
# import re,collections
# file = "//Users//immoralay//Desktop//文件.docx"
# def get_words(file):
#     with open(file) as f:
#         all_words = []
#         for i in f:
#             all_words.extend(re.split(r'[;\.\s]*'),i)
#         new_all_words = []
#         for l in f:
#             new_all_words.append(l)
#     return collections.Counter(new_all_words)
# print(get_words('文件.docx'))

from operator import itemgetter
f = open("/Users/immoralay/Desktop/python_study/111")
lines = f.read()#读取文章内容
article = lines.split()#将文中的内容切开来以单词形式组成一个列表
total = {}#定义一个字典
for words in article:
    total[words]= total.get(words,0)+1 #字典里存储key和value
#end_list = sorted(total.items(),key=itemgetter(1),reverse=True)#itemgetter(0)，获取key  itemgetter(1)，获取value
print(sorted(total.items(),key=itemgetter(1),reverse=True)[0:5])#items()这个函数，把字典形式的键、值，存在了一个元组内
# def histrogram_2(s):
#     d = dict()
#     for c in s:
#         d[c] = d.get(c, 0) + 1  # 当字符c自一次出现，由于字典d中没有c，d.get(c, 0)返回默认值0，d[c]的值变为1，其后d.get(c, 0)都都不再返回默认值，而返回d[c]的对于值并加一
#     return d

# str1 = 'Danphnis love Alice'#给出字符串
# d = {} #给出字典
# for x in str1:
#     if x in d:
#        d[x]=d[x]+1
#     else:
#        d[x]=1
# print (d)
























