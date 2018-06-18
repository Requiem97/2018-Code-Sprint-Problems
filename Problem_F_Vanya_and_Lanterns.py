try:
    inp = [int(x) for x in input().split(" ")]
    if len(inp) > 2: 
        print("Invalid Input.")
        exit()
    lanterns = [int(x) for x in input().split(" ")]
    if len(lanterns) > inp[0]:
        print("Too many lanterns")
        exit()
    lanterns.sort()
    if lanterns[0] < 0 or lanterns[-1] > inp[1]:
        print("Improper lantern location")
        exit()
    dist = []
    for i in range(len(lanterns)-1):
        dist.append(abs(lanterns[i] - lanterns[i+1])/2)
    dist.sort()
    dist.append(lanterns[0])
    dist.append(abs(lanterns[-1] - inp[1]))
    print(max(dist))
except ValueError:
    print("Invalid Input")