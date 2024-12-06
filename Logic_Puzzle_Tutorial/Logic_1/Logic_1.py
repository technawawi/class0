print('==== LOGIC 1 ====')
print()

SIZE = 9

print('Soal 1')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if (row == col) else ' ', end = '')
    print()
print()

print('Soal 2')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if (row + col == SIZE + 1) else ' ', end = '')
    print()
print()

print('Soal 3')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if (row == col or row + col == SIZE + 1) else ' ', end = '')
    print()
print()

print('Soal 4')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if (row == col or row + col == SIZE + 1 or row == 5 or col == 5) else ' ', end = '')
    print()
print()

print('Soal 5')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if (row >= col) else ' ', end = '')
    print()
print()

print('Soal 6')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if (row + col >= SIZE + 1) else ' ', end = '')
    print()
print()

print('Soal 7')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if ((row <= col and row + col <= SIZE + 1) or (row >= col and row + col >= SIZE + 1)) else ' ', end = '')
    print()
print()

print('Soal 8')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if ((row >= col and row + col <= SIZE + 1) or (row <= col and row + col >= SIZE + 1)) else ' ', end = '')
    print()
print()