a = int(input())
b = {}
d = []
for i in range(a):
    c = input().split()
    # split()通过指定分隔符对字符串进行切片，如果参数num有指定值，则仅分隔num个子字符串
    b[int(c[2])] = c[0] + ' ' + c[1]

for k in b:
    d.append(k)

print(b[max(d)])
print(b[min(d)])