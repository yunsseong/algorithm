expression = input()

tmp = ""
ans = 0
minus_flag = False
for i, x in enumerate(expression):
    if i == 0 and not x.isdigit():
        minus_flag = True
        continue

    if x.isdigit():
        tmp += x
    else:
        if minus_flag:
            ans -= int(tmp)
        else:
            ans += int(tmp)
        if x == "-":
            minus_flag = True
        tmp = ""

if minus_flag:
    ans -= int(tmp)
else:
    ans += int(tmp)
print(ans)