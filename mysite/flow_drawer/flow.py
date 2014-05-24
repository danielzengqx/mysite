#!/usr/bin/python


b = 'abc   abcd         efg'

a = b.split()
space=[]
tmp =b
for i in a:
    space.append(len(i)/2 * ' ' + '|' + (len(i)-len(i)/2-1)*' ')



for i in range(len(a)):
    tmp = tmp.replace(a[i],space[i],1)



print tmp,'\n',b
