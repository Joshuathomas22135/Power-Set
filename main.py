arr = [4,6,8]
n = len(arr)

for i in range(2**n):
    binary = format(i,f"0{n}b")
    subs = []
    for j in range(n):
        if i & (1<<j):
            subs.append(arr[j])
    print(binary, subs)