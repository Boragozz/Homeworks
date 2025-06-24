# Task 1
a = ['mon', 'tue', 'wen', 'thu', 'fry', 'sat', 'sun']
b = int(input('Введите число от 1 до 7: '))

if 1 <= b <= 7:
    print(a[b-1])
if b<1 or b >7:
    print("1 to 7 only, Okay???")
# Task 2
d = ['January', 'Fabruary', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December']
e = int(input('Enter a months number: '))
if e<1 or e >12:
    print("1 to 12 ...OMG, bro:-(")
if 1 <= e <= 12:
    print(d[e-1])
# Task 3
nu = int(input('Enter a number: '))
if nu < 0:
    print("Number is negative")
if nu > 0:
    print("Number is positive")
if nu == 0:
    print("Number is equal to zero")
# Task 4
f = int(input('Enter a first number: '))
j = int(input('Enter a second number: '))
if f != j and f > j:
    print(j,f)
if f != j and f < j:
    print(f,j)
