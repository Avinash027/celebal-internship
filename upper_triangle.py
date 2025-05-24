
n = int(input("Enter the number of rows for upper triangle: "))
print("\nUpper Triangular Pattern:")

for i in range(n):
    
    for j in range(i):
        print(" ", end=" ")
    
    for j in range(n - i):
        print("*", end=" ")
    print()
