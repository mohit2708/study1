array = ['orange', 'red', 'blue', 'orange', 'red', 'blue', 'green', 'red', 'blue', 'red']


# Count how many times each color appears
counts = {}
for color in array:
    if color in counts:
        counts[color] += 1
    else:
        counts[color] = 1

print(counts)
# Get the unique colors
unique_colors = []
for color in array:
    if color not in unique_colors:
        unique_colors.append(color)

print(unique_colors)

# Sort colors by their count using a simple bubble sort
for i in range(len(unique_colors)):
    for j in range(0, len(unique_colors) - i - 1):
        if counts[unique_colors[j]] > counts[unique_colors[j + 1]]:
            # Swap
            unique_colors[j], unique_colors[j + 1] = unique_colors[j + 1], unique_colors[j]

# Make the result list with repeated colors
result = []
for color in unique_colors:
    for _ in range(counts[color]):
        result.append(color)

print(result)

