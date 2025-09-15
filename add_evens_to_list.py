# 8. Add all even numbers from 1 to 100 to list

evens = []
for i in range(1, 101):
    if i % 2 == 0:
        evens.append(i)

print(evens)