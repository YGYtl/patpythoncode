number = int(input())
a = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
sum = 0
output = 0
while number != 0:
    dan = number % 10
    sum += dan
    number = number // 10

b = ''
r = str(sum)
for i in r:
    b += a[int(i)] + " "
print(b[0:-1])
