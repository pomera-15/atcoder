c = []
for x in range(0, 3):
    c.append(list(map(int, input().split())))

res = "Yes"
if not(c[0][0] - c[1][0] == c[0][1] - c[1][1] == c[0][2] - c[1][2]):
    res = "No"
if not(c[0][0] - c[2][0] == c[0][1] - c[2][1] == c[0][2] - c[2][2]):
    res = "No"
if not(c[2][0] - c[0][0] == c[2][1] - c[0][1] == c[2][2] - c[0][2]):
    res = "No"

if not(c[0][0] - c[0][1] == c[1][0] - c[1][1] == c[2][0] - c[2][1]):
    res = "No"
if not(c[0][1] - c[0][2] == c[1][1] - c[1][2] == c[2][1] - c[2][2]):
    res = "No"
if not(c[0][2] - c[0][0] == c[1][2] - c[1][0] == c[2][2] - c[2][0]):
    res = "No"

print(res)