arr = "abcdefghijklmnopqrstuwxyz"

key = 1
plain = "a"
cyper = ""
for c in plain:
    if c.isalpha():
        cyper += arr[(arr.index(c) + 1) % 26]

print(cyper)
