print('==== LOGIC 4 ====')
print('\n')

# Konstanta
SIZE = 9
HALF_SIZE = 5

# Soal 1
print('Soal 1')
print()
for row in range(1, HALF_SIZE + 1):
    for col in range(1, 2 * HALF_SIZE):
        if HALF_SIZE - row < col < HALF_SIZE + row:
            num = col - (HALF_SIZE - row)
            print(num, end='')
        else:
            print(' ', end='')
    print()
print('\n\n')





# Soal 2
print('Soal 2')
print()
for row in range(1, SIZE - 3):
    for col in range(1, SIZE + 1):
        if row <= col and row + col <= SIZE + 1:
            print(col - row + 1, end='')
        else:
            print(' ', end='')
    print()
print('\n\n')





# Soal 3
print('Soal 3')
print()
for row in range(1, HALF_SIZE + 1):
    for col in range(1, 2 * HALF_SIZE):
        if HALF_SIZE - row < col < HALF_SIZE + row:
            print(col - (HALF_SIZE - row), end='')
        else:
            print(' ', end='')
    print()
for row in range(HALF_SIZE - 1, 0, -1):
    for col in range(1, 2 * HALF_SIZE):
        if HALF_SIZE - row < col < HALF_SIZE + row:
            print(col - (HALF_SIZE - row), end='')
        else:
            print(' ', end='')
    print()
print('\n\n')





# Soal 4
print('Soal 4')
print()
for row in range(1, HALF_SIZE + 1):
    for col in range(1, 2 * HALF_SIZE):
        if HALF_SIZE - row < col < HALF_SIZE + row:
            num = row - abs(HALF_SIZE - col)
            print(2 * num - 1, end='')
        else:
            print(' ', end='')
    print()
print('\n\n')





# Soal 5
print('Soal 5')
print()
for row in range(HALF_SIZE, 0, -1):
    for space in range(HALF_SIZE - row):
        print(' ', end='')
    for col in range(1, 2 * row):
        num = 2 * col - 1
        if num <= (2 * row - 1):
            print(num, end='')
    for col in range(2 * row - 3, 0, -2):
        print(col, end='')
    print()
print('\n\n')





# Soal 6
print('Soal 6')
print()
for row in range(1, HALF_SIZE + 1):
    for space in range(HALF_SIZE - row):
        print(' ', end='')
    for col in range(1, row + 1):
        num = 2 * col - 1
        print(num, end='')
    for col in range(row - 1, 0, -1):
        num = 2 * col - 1
        print(num, end='')
    print()
for row in range(HALF_SIZE - 1, 0, -1):
    for space in range(HALF_SIZE - row):
        print(' ', end='')
    for col in range(1, row + 1):
        num = 2 * col - 1
        print(num, end='')
    for col in range(row - 1, 0, -1):
        num = 2 * col - 1
        print(num, end='')
    print()
print('\n\n')





# Soal 7
print('Soal 7')
print()

def crange(a, b):
    return range(a, b + 1)

def printnln(a):
    print(a, end='')

def ganjil(a):
    return a * 2 - 1

def pbound(a):
    return a - 1

def fib(a):
    if a <= 2:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)


for y in crange(-4, 4):
    for i in range(2):
        for s in crange(1, abs(y)):
            if i == 1 and s == 1:
                continue
            printnln(' ')

        n = 5 - abs(y)
        b = pbound(n)
        for x in crange(-b, b):
            if i == 1 and x == -4:
                continue
            c = n - abs(x)
            printnln(ganjil(c))

        for s in crange(1, abs(y)):
            printnln(' ')

    print()
print('\n\n')





# Soal 8
print('Soal 8')
print()

for y in crange(-4, 4):
    for i in range(2):
        for s in crange(1, abs(y)):
            if i == 1 and s == 1:
                continue
            printnln(' ')

        b = 4 - abs(y)
        for x in crange(-b, b):
            if i == 1 and x == -4:
                continue
            v = abs(x) + abs(y)
            if v % 2 == 1:
                printnln(' ')
            else:
                yn = abs(y) + 1
                nr = (5 - v) // 2 + 1
                mx = max(nr, yn)
                printnln(fib(mx))

        for s in crange(1, abs(y)):
            printnln(' ')

    print()