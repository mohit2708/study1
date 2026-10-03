### **add one digit**
```python
def add_one_to_digits(digits):
    # Start from the last digit
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:  # If the current digit is less than 9
            digits[i] += 1  # Just add 1
            return digits
        else:  # If the current digit is 9
            digits[i] = 0  # Set it to 0 and carry over 1

    # If we've exhausted all digits and still have a carry
    return [1] + digits  # Prepend 1 to the list (e.g., from 999 to 1000)

# Example input
example_list = [1,2,7]
result = add_one_to_digits(example_list)

print("Output:", result) # Output: [1, 2, 8]
```