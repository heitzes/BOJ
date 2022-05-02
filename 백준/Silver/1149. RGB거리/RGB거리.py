n = int(input())
RGB = []
for i in range(n):
    rgb = list(map(int, input().split()))
    RGB.append(rgb)
for k in range(1,n):
    RGB[k][0] = RGB[k][0] + min(RGB[k-1][1], RGB[k-1][2])
    RGB[k][1] = RGB[k][1] + min(RGB[k-1][2], RGB[k-1][0])
    RGB[k][2] = RGB[k][2] + min(RGB[k-1][0], RGB[k-1][1])
print(min(RGB[-1]))