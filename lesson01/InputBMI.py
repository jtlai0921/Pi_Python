h = input('請輸入身高: ')
w = input('請輸入體重: ')
print(h, w)

h = float(h)
w = float(w)
bmi = w / (h/100)**2
print("{0:.2f}".format(bmi))

if 18 <= bmi< 23:
    print('正常')
elif bmi >= 23:
    print('過重')
else:
    print('過輕')