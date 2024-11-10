result = []

def divider(a, b):
    if a < b:
        raise ValueError("a must be greater than or equal to b")
    if b > 100:
        raise IndexError("b must be 100 or less")
    return a / b
data = {10: 2, 2: 5, 123: 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        result.append(res)
    except (TypeError, ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Error for key={key}, value={value}: {e}")

print("Result:", result)
