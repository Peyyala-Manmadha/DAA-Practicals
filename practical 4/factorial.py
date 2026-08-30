import time


# Iterative Factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Recursive Factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Main Program
print("=" * 55)
print("FACTORIAL - ITERATIVE AND RECURSIVE")
print("=" * 55)

n = int(input("Enter a positive integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Iterative method
    start = time.perf_counter()
    iterative_result = factorial_iterative(n)
    iterative_time = time.perf_counter() - start

    # Recursive method
    start = time.perf_counter()
    recursive_result = factorial_recursive(n)
    recursive_time = time.perf_counter() - start

    print("\nFactorial using Iterative Method :", iterative_result)
    print("Factorial using Recursive Method :", recursive_result)

    print("\nTime Analysis:")
    print(f"Iterative Execution Time : {iterative_time:.10f} seconds")
    print(f"Recursive Execution Time : {recursive_time:.10f} seconds")

    print("\nTime Complexity:")
    print("Iterative Method : O(n)")
    print("Recursive Method : O(n)")

    print("\nSpace Complexity:")
    print("Iterative Method : O(1)")
    print("Recursive Method : O(n)")

print("=" * 55)
