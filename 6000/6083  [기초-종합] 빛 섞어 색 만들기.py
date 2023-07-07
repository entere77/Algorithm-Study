input_list = list(map(int, input().split()))
total = 0
for i in range(input_list[0]):
    for j in range(input_list[1]):
        for k in range(input_list[2]):
            print(f"{i} {j} {k}")
            total += 1
print(total)
