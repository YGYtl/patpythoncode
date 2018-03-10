a = input().split()
n = int(a[0])
q = int(a[1])
b = input().split()
c = []
for i in b:
    c.append(int(i))
c.sort()
l = n
mx = 0
for i in range(l):
    m_q = c[i]*q
    n_t = mx + i
    if n_t >= l:
        break
    for j in range(n_t, l):
        if c[j] <= m_q:
            mx += 1
        else:
            break
print(mx)