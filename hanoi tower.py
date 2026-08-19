def hanoi(n,source,auxiliary,destination):
    if n == 1:
        print(f"move disk from {source} to {destination}")
    else:
        hanoi(n-1,source,destination,auxiliary)
        print(f"move disk from {source} to {destination}")
        hanoi(n-1,auxiliary,source,destination)
hanoi(3,"A","B","C")
