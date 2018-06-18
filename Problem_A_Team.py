input_size = int(input())
inp = []
implement_number = 0
for i in range(input_size):
    line = input().split(" ")
    if len(line) > 3:
        print("Invalid Input")
        break
    else:
        inp.append(line)
        count = 0
        for j in inp[i]:
            if j == "1":
                count += 1
            else:
                pass
        if count > 1: implement_number += 1
print(implement_number)