# -*- coding:UTF-8 -*-
import keyword
import random
import math;

print("我是中文")

h = 170 # int
w = 60.5 # float
x = 12649216492164919419822131241241221359275027357237529357982356982365326562352 # int -> long -> 無限(根據內存)
bmi = w / (h/100)**2
print(bmi)
bmi = w / math.pow(h/100, 2)
print(bmi)


print(type(h)) # 檢視資料型別
print(type(w))
print(type(x))

age, name = 28, 'python'
print(age, name)

flag = True # True = 1, False = 0
count = 5
print(count + flag)

#del count

print(keyword.kwlist) # 列出 keyword
print(keyword.iskeyword('assert')) # 判斷是否為 keyword

# 資料轉型
x = '100'
y = '90'
sum = int(x) + int(y)
print(sum)
msg = 'sum=' + str(sum)
print(msg)

n = random.randint(1, 10)
print(n)

print('台積電')
print(180.5, '台積電', 5000)
print(180.5, '台積電', 5000, sep='&')
print(180.5, '台積電', 5000, sep='&', end=';')
print(180.5, '台積電', 5000, sep='&')
print('%s 價格 %.1f 買 %03d 張' % ('台積電', 180.5, 5))
print('%s 價格 %.1f 買 %03d 張 共需 $%.1f' % ('台積電', 180.5, 50, (180.5*50*1000)))
print('%s 價格 %.1f 買 %03d 張 共需 $%.1f' % ('台積電', 180.5, 500, (180.5*500*1000)))

name = 'python'
version = 3.615
print("Output : {0} {1}".format(name, version))
print("Output : {0} {1:.2f}".format(name, version))

number = random.randint(1, 100)
msg = "偶數" if number % 2 == 0 else "奇數"
print(number, msg)
