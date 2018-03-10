n, m = input().split()
n, m = int(n), int(m)

v_list, e_list, w_list = [], [], []

for i in range(m):
    e_list.append(0)
    string = input().split()
    v_list.append(string[0])
    w_list.append(string[2:])

for i in range(n):
    sum = 0
    string = input()
    string = string[1:-1]
    string = string.split(') (')
    for j in range(m):
        k = ' '.join(w_list[j])
        if k == string[j]:
            sum += int(v_list[j])
        else:
            e_list[j] += 1
    print(sum)

mx = max(e_list)
if mx == 0:
    print("Too simple")
else:
    print(mx, end='')
    for i in range(0, m):
        if e_list[i] == mx:
            print(' ' + str(i+1), end='')