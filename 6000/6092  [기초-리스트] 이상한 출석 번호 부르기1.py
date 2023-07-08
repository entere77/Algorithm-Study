n = int(input())
ranN = list(map(int, input().split()))

answer = 23*[0]

for k in ranN:
    answer[k-1] += 1
print(*answer)
