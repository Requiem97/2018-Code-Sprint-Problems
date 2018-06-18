try:
    n = int(input())
    inp = input()
    queue = [int(x) for x in inp.split(" ")]
    if len(queue) > n: print("Invalid Input!\nNumber of elements must be at most", n)
    else:
        sum = 0
        count = 0
        queue.sort()
        for i in queue:
            if i >= sum:
                sum += i
                count += 1
        print(count)

except ValueError:
    print("Invalid Input")
