a = []
for _ in range(28):
    a.append(int(input()))
for _ in range(1, 31):
    if _ not in a:
        print(_)
