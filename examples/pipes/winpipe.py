with open(r"\\.\pipe\lithium-COM1") as f:
    while True:
        b = f.read(1)
        print(b)
