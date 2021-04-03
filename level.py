lv = 1
exp = 100
plus = 1.5
maxlev = 200

f = open('txt/level.txt', 'a')
print("1~40(5%)", file=f)
print("41~80(7%)", file=f)
print("81~120(5%)", file=f)
print("121~160(7%)", file=f)
print("161~180(4%)", file=f)
print("181~200(6%)", file=f)

while lv < 41:
    print(lv, "=", int(exp), file=f)
    lv = lv + 1
    exp = exp * 1.05

while lv < 81:
    print(lv, "=", int(exp), file=f)
    lv = lv + 1
    exp = exp * 1.07

while lv < 121:
    print(lv, "=", int(exp), file=f)
    lv = lv + 1
    exp = exp * 1.05

while lv < 161:
    print(lv, "=", int(exp), file=f)
    lv = lv + 1
    exp = exp * 1.07

while lv < 181:
    print(lv, "=", int(exp), file=f)
    lv = lv + 1
    exp = exp * 1.04

while lv < 201:
    print(lv, "=", int(exp), file=f)
    lv = lv + 1
    exp = exp * 1.06
