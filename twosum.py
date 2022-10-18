
def twosum(a,target):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] + a[j] == target:
                return [i, j]

a =[1,2,4]
target = 6

print(twosum(a, target))