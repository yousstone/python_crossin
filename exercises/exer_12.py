import re
f1 = open('form.txt')
data = f1.read()
f1.close()

result = re.findall('[A-z]+',data)

result.sort()
data = '\n'.join(result)

f2 = open('fo.txt', 'w')
f2.write(data)
f2.close()
