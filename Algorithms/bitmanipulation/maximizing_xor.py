l = int(input())
r = int(input())
output = 0
for i in range(l, r + 1):
    for j in range(l, r + 1):
        output = max(output, i ^ j)
print(output)