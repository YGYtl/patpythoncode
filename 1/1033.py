a = input()
b = input()
a = list(a)
b = list(b)
c = []
o=0
for i in a:
    if '+' in a:
        o = 1
    if i>='A'and i<='Z':
        l = i.lower()
        a.append(l)

for i in b:
    if o == 1 and (i>='A'and i<='Z'):
        continue
    if i not in a:
        c.append(i)

print(''.join(c))