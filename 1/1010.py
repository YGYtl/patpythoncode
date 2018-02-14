a = input().split()
l = len(a)
m = 0
for i in range(0, l, 2):
    if m == 0 and int(a[i+1]) == 0:
        print("0 0")
    if int(a[i+1]) != 0:
        if m == 1:
            print(" ", end='')
        print(str(int(a[i])*int(a[i+1])) + ' ' + str(int(a[i+1])-1), end='')
        m = 1