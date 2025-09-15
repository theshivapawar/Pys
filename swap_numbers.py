# 1. Swap two numbers
# Using addition and subtraction
a = 1
b = 2
a = a + b
b = a - b
a = a - b
print(a, b)

# Using multiplication and division
c = 3
d = 4
c = c * d
d = c // d
c = c // d
print(c, d)

# Without using a third variable
e = 5
f = 6
e, f = f, e
print(e, f)

# Using a third variable
g = 7
h = 8
temp = g
g = h
h = temp
print(g, h)