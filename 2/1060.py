n = int(input())
a = input().split()
b = []
for i in a:
    b.append(int(i))
b = sorted(b)
b.reverse()
m = 0
c = 1
while m < n and b[m] > c:
    c += 1
    m += 1
print(m)