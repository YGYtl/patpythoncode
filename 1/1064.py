a = int(input())
b = input().split()
c = []
for i in b:
    k = int(i)
    sum_ = 0
    while k:
        sum_ = sum_ + k%10
        k = k // 10
    if sum_ not in c:
        c.append(sum_)
c.sort()
l = len(c)
print(l)
for i in range(0, l):
    print(str(c[i]), end='')
    if i != l - 1:
        print(' ', end='')