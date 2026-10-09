def check_beam(load):
    if load > 1000:
        return "risk"
    return "safe"

result = []
for load in (500, 1200, 800):
    result.append(f"{load}: {check_beam(load)}")
    print(load, check_beam(load))

with open("result.txt", "w") as f:
    f.write(str(result))
