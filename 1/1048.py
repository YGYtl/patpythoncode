a = input().split()
A = a[0]
B = a[1]
A = list(A[::-1])
B = list(B[::-1])
c = []
l1 = len(A)
l2 = len(B)
mx = max(l1, l2)

if l1 > l2:
    for i in range(l2, l1):
        B.append('0')
elif l1 < l2:
    for i in range(l1, l2):
        A.append('0')

k = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
for i in range(0, mx):
    if i % 2 == 0:
        c += k[(int(A[i])+int(B[i]))%13]
    else:
        m = int(B[i]) - int(A[i])
        if m < 0:
            m = m + 10
        c.append(str(m))

print(''.join(list(reversed(c))))