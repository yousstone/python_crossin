# coding=utf-8
print "乘法表"
muti = 1
for i in range(1,10):
	for j in range(1,i+1):
		muti = j * i
		print "%s * %s = %s"%(j,i,muti),' ',
	print
