# coding=utf8

import random
print "从1~n中，随机取m个数。1<=m<=n "

print "please enter an integer for n: "

n=input()

print "please enter an integer for m: "

m=input()

list_1=[]
list_2=[]
print "方法一"

for i in range(0,m):
	a=random.randint(1,n)
	list_1.append(a)
	if a not in list_2:
		list_2.append(a)

print "list_1 原始数据：%s \n"%list_1
print "list_1 排序后数据：%s \n"%sorted(list_1)
print 
print "list_2(去重) 原始数据：%s \n"%list_2
print "list_2(去重) 排序后数据：%s \n"%sorted(list_2)

print "方法二：简洁的方法如下："

f2=random.sample(range(1,n+1),m)# random.sample可去除重复值
print f2
print sorted(f2)

print "\n方法三："

list_3=[]
for i in range(0,m):
	list_3.append(random.randint(1,n))
print "list is \n %s\n"%list_3
print "set(list) is \n %s\n"%set(list_3)
print "sorted(set(list)) is \n %s\n"%sorted(set(list_3))

