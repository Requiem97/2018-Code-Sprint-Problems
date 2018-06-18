inp = []
for i in range(2):
    inp.append(input().split(" "))
n = int(inp[0][0])
k = int(inp[0][1])
if n in range(0, 2001) and k in range(0,6):
    if len(inp[0]) > 2 or len(inp[1]) > n: print ("Invalid Input")
    else:
        limit = 5 - k
        member_count = 0
        team_count = 0
        inp[1].sort()
        for i in inp[1]:
            if int(i) <= limit: member_count += 1
            else: break
            if member_count == 3:
                team_count += 1
                member_count = 0
        print(team_count)
else: print("Invalid Range. Must be:\n1 <= n <=2000\n1 <= k <= 5")