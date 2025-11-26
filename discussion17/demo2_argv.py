import sys

print("Number of arguments:", len(sys.argv))
print("Argument List:", sys.argv)

for i, arg in enumerate(sys.argv):
    print(f"Argument {i}: {arg}")