# Matrix Chain Multiplication using Dynamic Programming

print("=" * 60)
print("MATRIX CHAIN MULTIPLICATION USING DYNAMIC PROGRAMMING")
print("=" * 60)

# Number of matrices
n = int(input("Enter number of matrices: "))

# Dimensions of matrices
print("\nEnter dimensions:")
dimensions = []

for i in range(n + 1):
    d = int(input(f"Enter dimension {i + 1}: "))
    dimensions.append(d)

# DP table
dp = [[0 for _ in range(n)] for _ in range(n)]

# Calculate minimum multiplication cost
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')

        for k in range(i, j):
            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
            )

            dp[i][j] = min(dp[i][j], cost)

# Display result
print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print("Minimum number of scalar multiplications:", dp[0][n - 1])

print("\nTime Complexity: O(n^3)")
print("Space Complexity: O(n^2)")

print("=" * 60)
