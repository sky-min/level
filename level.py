lv = 1
exp = 100
plus = 110/100
maxlev = 200

f = open('10per.txt', 'a')
print("=====10%=====", file=f)

while lv < maxlev + 1:
    print(lv, "=", int(exp), file=f)
    lv = lv + 1
    exp = exp * plus
