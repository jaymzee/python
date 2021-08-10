with open(r"\\.\pipe\lithium-COM1") as f:
    while True:
        b = f.read(1)
        if len(b) == 0:
            break
        print(b)
