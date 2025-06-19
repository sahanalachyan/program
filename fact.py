def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    result = 1
    for i in range(2, n + 1):   # 0! and 1! both return 1
        result *= i
    return result

# Example
print(factorial_iter(5))   # → 120
