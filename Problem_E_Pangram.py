def is_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string:
            return "NO"
    return "YES"
try:
    n = int(input())
    string = input()
    if len(string) != n: print("n and string lenght does not match")
    else:
        if len(string) < 26: print("NO")
        else: print(is_pangram(string.lower()))
except ValueError:
    print("Invalid Input")