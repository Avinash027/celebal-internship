
n = int(input("Enter the number of rows for lower triangle: "))
print("\nLower Triangular Pattern:")

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
