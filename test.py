print("for:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")

print("while:")
i = 1
while i < 11:
    j = 1
    while j < 11:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
    