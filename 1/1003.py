list = []
a = []
n = int(input())
for i in range(0, n):
    list.append(input())

for i in range(0, n):
    l = len(list[i])
    c1 = 0
    c2 = 0
    c3 = 0
    for u in range(0, l):
        if list[i][u] == 'P':
            c1 += 1
        elif list[i][u] == 'T':
            c2 += 1
        elif list[i][u] == 'A':
            c3 += 1
    if l == c1 + c2 + c3 and c1 ==1 and c2 == 1 and c3 != 0:
        a.append(1)
    else:
        a.append(0)

def f(o):
    l2 = len(o)
    l_p = o.find('P')
    l_t = o.find('T')
    if l_t - l_p == 2 and l_p == l2 - l_t - 1:
        return 1
    else:
        if l_p*(l_t - l_p - 1) == l2 - l_t - 1:
            return 1
        else:
            return 0

for i in range(0, n):
    if a[i] == 0:
        print('NO')
    else:
        if f(list[i]) == 1:
            print('YES')
        else:
            print('NO')