num = int(input())
if num < 0:
    if num % 2:
        print("B")
    else:
        print("A")
else:
    if num % 2:
        print("D")
    else:
        print("C")
