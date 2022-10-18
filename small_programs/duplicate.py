a = [-11, 13, 13, 10, -11, 10, 9, -3, 6, -9, -6, -6, 13, 8, -11, -5, 6, -8, -12, 5, -9, -1, -5, 2, -2, 13, 14, -9, 7,
     -4]


def unique(a):
    a = set(a)
    print(list(a))


unique(a)

# to maintain same order
b = list()
for i in a:
    if i not in b:
        b.append(i)

print(b)
