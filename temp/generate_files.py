import os

for i in range(35, 35):  # 36 to 52 inclusive
    filename = f"a3q{i}.py"
    with open(filename, "w") as f:
        f.write('print("Name = Ritesh Dhekane")\n')
    print(f"Created {filename}")
