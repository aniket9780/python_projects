add_10 = lambda x: x + 10

mult = lambda x, y: x * y

point2d = [(4, 5), (1, 6), (5, -1), (4, 8), (12, 9), (23, 46)]
point2d_sort = sorted(point2d)
print(point2d_sort)
point2d_sort_second = sorted(point2d, key=lambda x: x[1])
print(point2d_sort_second)

sorted_sum = sorted(point2d, key=lambda x: x[0] + x[1])
print(sorted_sum)
