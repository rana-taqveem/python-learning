def sqrt_binary_search(n, precision):
    low = 0.0
    high = max(1.0, n)  # Handle cases where n < 1
    while high - low > precision:
        mid = (low + high) / 2
        square = mid * mid
        if square == n:
            return mid
        elif square < n:
            low = mid
        else:
            high = mid
    return (low + high) / 2

result = sqrt_binary_search(10, 0.001)
print(f"The square root of 10 is approximately: {result}")