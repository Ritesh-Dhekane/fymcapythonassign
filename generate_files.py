import os

for i in range(8, 35):  # 8 to 34 inclusive
    filename = f"a2q{i}.py"
    with open(filename, "w") as f:
        f.write('print("Name = Ritesh Dhekane")\n')
    print(f"Created {filename}")
