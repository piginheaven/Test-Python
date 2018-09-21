import os
import sys

print("请输入路径名:")
dirname=input()
print("得到路径名%s"%(dirname))
list=os.listdir(dirname)
for i in range(0,len(list)):
	path=os.path.join(dirname,list[i])
	print(path)
	

print("请输入文件名:")
filename=input()
print("即将处理%20s:"%(filename))

with open(filename, 'r', encoding="utf-8") as f:
    i = 0
    for row_ in f:
        row = row_.strip().encode("utf-8").decode("utf-8")
        i += 1

print("\n")
print("\n")
print("\n")
print("\n")

#try:
f=open(filename,'r',encoding='utf-8',errors='ignore')
text=f.readlines()
#text=''.join(text).strip('\n')
print(text[0])
#abcline=f.read()
#print("%s",%(abcline)) 
#finally:
#    if f: 
f.close()
	