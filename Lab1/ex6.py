range1 = list(range(0, 7))
print('range1:', end=' ')
print(*range1, sep=', ')

range2 = list(range(1, 11, 3))
print('range2:', end=' ')
print(*range2, sep=', ')

range3 = list(range(5, 0, -1))
print('range3:', end=' ')
print(*range3, sep=', ')

range4 = list(range(6, -3, -2))
print('range4:', end=' ')
print(*range4, sep=', ')