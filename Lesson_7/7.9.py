import numpy

a = numpy.random.randint(1, 20, size=(3, 3))
b = numpy.random.randint(1, 20, size=(3, 3))
print(a)
print(b)
# Using lib numpy
print(a.dot(b))
# Manually
c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        element = 0
        for k in range(3):
            element += a[i][k] * b[k][j]
            # print(f"a[{i+1}][{k+1}] * b[{k+1}][{j+1}]")
        c[i][j] = element
c = numpy.array(c)
print(c)
